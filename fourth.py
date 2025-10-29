def je_tah_mozny_strelec(pozice, cilova_pozice, obsazene_pozice):
    r1, s1 = pozice
    r2, s2 = cilova_pozice
    if abs(r2 - r1) != abs(s2 - s1):
        return False

    krok_r = 1 if r2 > r1 else -1
    krok_s = 1 if s2 > s1 else -1
    for i in range(1, abs(r2 - r1)):
        if (r1 + i * krok_r, s1 + i * krok_s) in obsazene_pozice:
            return False
    return True


def je_tah_mozny_vez(pozice, cilova_pozice, obsazene_pozice):
    r1, s1 = pozice
    r2, s2 = cilova_pozice

    if r1 != r2 and s1 != s2:
        return False

    if r1 == r2: 
        krok = 1 if s2 > s1 else -1
        for s in range(s1 + krok, s2, krok):
            if (r1, s) in obsazene_pozice:
                return False
    else:  # vertikální tah
        krok = 1 if r2 > r1 else -1
        for r in range(r1 + krok, r2, krok):
            if (r, s1) in obsazene_pozice:
                return False
    return True


def je_tah_mozny_dama(pozice, cilova_pozice, obsazene_pozice):
    return (
        je_tah_mozny_strelec(pozice, cilova_pozice, obsazene_pozice)
        or je_tah_mozny_vez(pozice, cilova_pozice, obsazene_pozice)
    )


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    pozice = figurka["pozice"]
    r2, s2 = cilova_pozice

    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    if typ == "pěšec":
        r1, s1 = pozice
        if s1 != s2:
            return False
        if r1 == 2 and cilova_pozice == (4, s1):  # dvojkrok ze startu
            if (3, s1) in obsazene_pozice:
                return False
            return True
        if cilova_pozice == (r1 + 1, s1):  # o jedno pole dopředu
            return True
        return False

    if typ == "jezdec":
        if (abs(cilova_pozice[0] - pozice[0]), abs(cilova_pozice[1] - pozice[1])) in [(2, 1), (1, 2)]:
            return True
        return False

    if typ == "věž":
        return je_tah_mozny_vez(pozice, cilova_pozice, obsazene_pozice)

    if typ == "střelec":
        return je_tah_mozny_strelec(pozice, cilova_pozice, obsazene_pozice)

    if typ == "dáma":
        return je_tah_mozny_dama(pozice, cilova_pozice, obsazene_pozice)

    if typ == "král":
        if abs(cilova_pozice[0] - pozice[0]) <= 1 and abs(cilova_pozice[1] - pozice[1]) <= 1:
            return True
        return False

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
