```python
def int_to_mini_roman(n):
    if n < 1000:
        result = []
        for i in range(0, n + 1):
            if i == 0:
                result.append("i")
            elif i == 5:
                result.append("v")
            elif i == 10:
                result.append("x")
            elif i == 25:
                result.append("xx")
            elif i == 50:
                result.append("l")
            elif i == 75:
                result.append("lx")
            elif i == 100:
                result.append("c")
            elif i == 125:
                result.append("cx")
            elif i == 150:
                result.append("cl")
            elif i == 175:
                result.append("clx")
            elif i == 200:
                result.append("cc")
            elif i == 225:
                result.append("ccx")
            elif i == 250:
                result.append("ccl")
            elif i == 275:
                result.append("cclx")
            elif i == 300:
                result.append("ccc")
            elif i == 325:
                result.append("cccx")
            elif i == 350:
                result.append("ccll")
            elif i == 375:
                result.append("ccllx")
            elif i == 400:
                result.append("cccc")
            elif i == 425:
                result.append("ccccx")
            elif i == 450:
                result.append("cclll")
            elif i == 475:
                result.append("cclllx")
            elif i == 500:
                result.append("vv")
            elif i == 525:
                result.append("vvx")
            elif i == 550:
                result.append("vl")
            elif i == 575:
                result.append("vlx")
            elif i == 600:
                result.append("vc")
            elif i == 625:
                result.append("vcx")
            elif i == 650:
                result.append("vcl")
            elif i == 675:
                result.append("vclx")
            elif i == 700:
                result.append("vvv")
            elif i == 725:
                result.append("vvvx")
            elif i == 750:
                result.append("vvl")
            elif i == 775:
                result.append("vvlx")
            elif i == 800:
                result.append("vvc")
            elif i == 825:
                result.append("vvcx")
            elif i == 850:
                result.append("vvcl")
            elif i == 875:
                result.append("vvclx")
            elif i == 900:
                result.append("vvvv")
            elif i == 925:
                result.append("vvvvx")
            elif i == 950:
                result.append("vvvl")
            elif i == 975:
                result.append("vvvlx")
            elif i == 1000:
                result.append("xxxx")
        return "".join(result)
    else:
        return "Error: Enter a number between 1 and 1000"
```

This code uses a nested loop to iterate through numbers from 1 to `n`, converting each number to its mini roman numeral representation piecemeal and concatenating the result. It ensures that numbers like 26, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750