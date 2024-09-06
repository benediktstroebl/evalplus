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
        elif i == 500:
            res.append("m")
        elif i == 1000:
            res.append("m")
        else:
            num = i % 5
            if num == 0:
                res.append("0")
            elif num == 1:
                res.append("i")
            elif num == 2:
                res.append("ii")
            elif num == 3:
                res.append("iii")
            elif num == 4:
                res.append("iv")

    return "".join(res)