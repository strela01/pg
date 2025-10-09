def prace_se_seznamem():
    #vytvorime seznam (list) o 4prvcich 
    seznam = [100,5,3,21]
    print(seznam)
    seznam[2] *= 2
    # vezneme 3. prvek a vynasobime ho 2
    print(seznam)
    seznam.append(55)

    seznam.sort()
    
    seznam.reverse()

    print(seznam)

def vrat_treti_prvek(seznam):
    if len(seznam) >= 3:
        return seznam[2] 
    else: 
        return None

def prumer(cisla):
    return sum(cisla) / len(cisla)

def naformuj_text(zak):
    jmeno = zak["jmeno"]
    prijemni = zak["prijmeni"]
    vek = zak["vek"]
    znamky = zak["znamky"]
    prumer_znamek = (prumer(znamky)
                     
        
    text = f"Student: {jmeno} {prijemni}, vek: {vek}, obor: {obor}, prumer: {prumer znamek}"
    return text

if __name__ == "__main__":

    student = {
    "jmeno": "Jan",
    "prijmeni": "Novak",
    "vek": 22,
    "znamky": [1,2,3,1,2,1]
    }
    student["vek"] += 1
    student["obor"] ="AEFP"
    print(naformuj_text(student))



