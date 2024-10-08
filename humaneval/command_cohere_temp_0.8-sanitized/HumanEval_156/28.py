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
        elif n - i < 10 and i % 5 == 0:
            res.append(".".join(map(str, [i // 5, '0' * 4])))