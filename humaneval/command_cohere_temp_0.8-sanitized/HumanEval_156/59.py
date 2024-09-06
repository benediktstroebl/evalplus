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
        elif i == 50:
            res.append("l")
        elif i == 100:
            res.append("c")
        elif i == 500:
            res.append("d")
        elif i == 1000:
            res.append("m")
        else:
            roman = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            for j in range(0, 13):
                if i >= roman[j] and i < roman[j + 1]:
                    num = int(str(roman[j + 1] - roman[j])[1:])
                    res.append(str(num))
                    i -= roman[j]
                    break

    return "".join(res)