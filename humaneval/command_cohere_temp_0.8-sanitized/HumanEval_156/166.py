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
                result.append("clvx")
            elif i == 400:
                result.append("cd")
            elif i == 425:
                result.append("cdov")
            elif i == 450:
                result.append("cdu")
            elif i == 475:
                result.append("cduv")
            elif i == 500:
                result.append("cdx")
            elif i == 525:
                result.append("cdxv")
            elif i == 550:
                result.append("cdxl")
            elif i == 575:
                result.append("cdxvl")
            elif i == 600:
                result.append("ce")
            elif i == 625:
                result.append("cve")
            elif i == 650:
                result.append("cv")
            elif i == 675:
                result.append("cvl")
            elif i == 700:
                result.append("cx")
            elif i == 725:
                result.append("cxv")
            elif i == 750:
                result.append("cxl")
            elif i == 775:
                result.append("cxvl")
            elif i == 800:
                result.append("cv")
            elif i == 825:
                result.append("cvx")
            elif i == 850:
                result.append("cvl")
            elif i == 875:
                result.append("cvvl")
            elif i == 900:
                result.append("cx")
            elif i == 925:
                result.append("cxv")
            elif i == 950:
                result.append("cxl")
            elif i == 975:
                result.append("cxvl")
            else:
                result.append("xx")
        return "".join(result)
    else:
        return "Invalid Input"