from flask import Flask, render_template, request
from items import item_rank, rank_gur
from keisan import keisan

app = Flask(__name__)

#履歴
history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global history

    if request.method == "POST":
        item = request.form.get("item")
        kosuu = request.form.get("kosuu")

        #未入力チェック
        if not item or not kosuu:
            return render_template(
                "index.html",
                items=item_rank.keys(),
                history=history,
                error="アイテム名と個数を入力してください"
            )
        
        #数字チェック
        if not kosuu.isdigit():
            return render_template(
                "index.html",
                items=item_rank.keys(),
                history=history,
                error="個数は正の整数で入力してください"
            )
        kosuu = int(kosuu)

        #0チェック
        if kosuu == 0:
            return render_template(
                "index.html",
                items=item_rank.keys(),
                history=history,
                error="1以上で入力してください"
            )
        
        #アイテムの存在チェック
        if item not in item_rank:
            return render_template(
                "index.html",
                items=item_rank.keys(),
                history=history,
                error="そのアイテムは存在しません"
            )

        #計算
        rank = item_rank[item]
        tanka = rank_gur[rank]

        enn, amari = keisan(tanka, kosuu)

        #履歴追加
        history.insert(0, {
            "item": item,
            "kosuu": kosuu,
            "enn": enn,
            "amari": amari
        })

        #履歴上限(5件)
        if len(history) > 5:
            history.pop()

        return render_template(
            "index.html",
            items=item_rank.keys(),
            history=history,
            result=f"{item}:{kosuu}個 買取価格 {enn}円 買取不可 {amari}個"
        )
    
    #GET
    return render_template(
        "index.html", 
        items=item_rank.keys(),
        history=history
        )


if __name__ == "__main__":
    app.run(debug=True)