import random

sonastik = {"koer": "собака", "kass": "кот", "lind": "птица", "jänes": "кролик", "karu": "медведь",}

def tolgi_est_rus(sona):
    """
    Tolgib sona eesti keeles vene keelde.
    """
    return sonastik.get(sona, "Sona ei ole leidnud")

def tolgi_rus_est(sona):
    """
    Tolgib sona vene keeles eesti keelde.
    """
    for est, rus in sonastik.items():
        if rus == sona:
            return est
    return "Sona ei ole leidnud"

def lisa_sona(est, rus):
    """
    Lisab uue sona sonastikku.
    """
    if est in sonastik:
        return "Sona juba on sonastikus"
    sonastik[est] = rus
    return "Sona on lisatud"

def paranda_sona(old_est, new_est, new_rus):
    """
    Parandab sona sonastikus.
    """
    if old_est not in sonastik:
        return "Sona ei ole leidnud"
    sonastik.pop(old_est)
    sonastik[new_est] = new_rus
    return "Sona on parandatud"

def testi_teadmisi():
    if not sonastik:
        return "Sonastik on tuhi"
    questions = list(sonastik.items())
    random.shuffle(questions)
    correct = 0
    total = len(questions)

    for est, rus in questions:
        answer = input(f"Kuidas tolgib '{est}' vene keelte? ")
        if answer.lower() == rus.lower():
            print("Oige!")
            correct += 1
        else:
            print(f"Vale. Oige vastus on: {rus}")

    print(f"Test on lopetatud! Teie result on: {round(correct / total * 100)}%")
