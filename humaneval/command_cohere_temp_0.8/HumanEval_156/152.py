```python
def int_to_mini_roman(num):
    if num < 1000:
        result = []
        for i in range(0, num + 1):
            if i == 0:
                result.append("i")
            elif i == 5:
                result.append("v")
            elif i == 10:
                result.append("x")
            elif i == 25:
                result.append("l")
            elif i == 50:
                result.append("c")
            elif i == 100:
                result.append("d")
            elif i == 125:
                result.append("dc")
            elif i == 150:
                result.append("cd")
            elif i == 175:
                result.append("cdl")
            elif i == 200:
                result.append("ce")
            elif i == 225:
                result.append("cve")
            elif i == 250:
                result.append("cv")
            elif i == 300:
                result.append("cx")
            elif i == 375:
                result.append("cxv")
            elif i == 400:
                result.append("cd")
                result.append("100")
            elif i == 425:
                result.append("cd")
                result.append("25")
                result.append("v")
            elif i == 450:
                result.append("cd")
                result.append("50")
                result.append("v")
            elif i == 475:
                result.append("cd")
                result.append("75")
                result.append("v")
            elif i == 500:
                result.append("cd")
                result.append("100")
                result.append("v")
            elif i == 525:
                result.append("cd")
                result.append("25")
                result.append("v")
                result.append("5")
            elif i == 550:
                result.append("cd")
                result.append("50")
                result.append("v")
                result.append("5")
            elif i == 575:
                result.append("cd")
                result.append("75")
                result.append("v")
                result.append("5")
            elif i == 600:
                result.append("ce")
                result.append("100")
            elif i == 625:
                result.append("cve")
                result.append("25")
                result.append("5")
            elif i == 650:
                result.append("cve")
                result.append("50")
                result.append("5")
            elif i == 675:
                result.append("cve")
                result.append("75")
                result.append("5")
            elif i == 700:
                result.append("cv")
                result.append("100")
            elif i == 725:
                result.append("cv")
                result.append("25")
                result.append("5")
            elif i == 750:
                result.append("cv")
                result.append("50")
                result.append("5")
            elif i == 775:
                result.append("cv")
                result.append("75")
                result.append("5")
            elif i == 800:
                result.append("cx")
                result.append("100")
            elif i == 825:
                result.append("cx")
                result.append("25")
                result.append("5")
            elif i == 850:
                result.append("cx")
                result.append("50")
                result.append("5")
            elif i == 875:
                result.append("cx")
                result.append("75")
                result.append("5")
            else:
                result.append("x")