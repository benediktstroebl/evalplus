```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for i in range(0, n + 1):
        if i == 0:
            res.append("i")
        elif i == 5:
            res.append("v")
        elif i == 10:
            res.append("x")
        elif i == 25:
            res.append("xx")
        elif i == 50:
            res.append("l")
        elif i == 75:
            res.append("lx")
        elif i == 100:
            res.append("c")
        elif i == 125:
            res.append("cx")
        elif i == 150:
            res.append("cl")
        elif i == 175:
            res.append("clx")
        elif i == 200:
            res.append("d")
        elif i == 225:
            res.append("dx")
        elif i == 250:
            res.append("dl")
        elif i == 275:
            res.append("dlx")
        elif i == 300:
            res.append("dc")
        elif i == 325:
            res.append("dcx")
        elif i == 350:
            res.append("dcl")
        elif i == 375:
            res.append("dclx")
        elif i == 400:
            res.append("cd")
        elif i == 425:
            res.append("cdx")
        elif i == 450:
            res.append("cdl")
        elif i == 475:
            res.append("cdlx")
        elif i == 500:
            res.append("cdv")
        elif i == 525:
            res.append("cdvx")
        elif i == 550:
            res.append("cdvl")
        elif i == 575:
            res.append("cdvlx")
        elif i == 600:
            res.append("cdvc")
        elif i == 625:
            res.append("cdvcx")
        elif i == 650:
            res.append("cdvcl")
        elif i == 675:
            res.append("cdvclx")
        elif i == 700:
            res.append("cdvcv")
        elif i == 725:
            res.append("cdvcvx")
        elif i == 750:
            res.append("cdvcvl")
        elif i == 775:
            res.append("cdvcvlx")
        elif i == 800:
            res.append("cve")
        elif i == 825:
            res.append("cvex")
        elif i == 850:
            res.append("cvel")
        elif i == 875:
            res.append("cvelx")
        elif i == 900:
            res.append("cvc")
        elif i == 925:
            res.append("cvcx")
        elif i == 950:
            res.append("cvl")
        elif i == 975:
            res.append("cvlx")
        elif i == 1000:
            res.append("cv")

        if i == n:
            break

    return "".join(res)
```

This code uses a nested loop to iterate through each digit of the integer `n`, and converts each digit to its mini-roman representation. The resulting roman numerals are concatenated to form the final result.