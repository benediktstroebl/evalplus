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
            res.append("l")
        elif i == 50:
            res.append("c")
        elif i == 100:
            res.append("d")
        elif i == 250:
            res.append("m")
        elif i == 500:
            res.append("m")
            res.append("d")
        elif i == 750:
            res.append("nd")
        elif i == 900:
            res.append("cm")
        elif i == 950:
            res.append("cd")
        elif i == 999:
            res.append("cm")
            res.append("d")
        elif i == 1000:
            res.append("k")
    return "".join(res)