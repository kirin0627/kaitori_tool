def keisan(tanka,kosuu):
    goukei = tanka * kosuu

    enn = int(goukei)

    amari_en = goukei % 1

    amari_kosu = int(amari_en / tanka)

    return enn, amari_kosu
