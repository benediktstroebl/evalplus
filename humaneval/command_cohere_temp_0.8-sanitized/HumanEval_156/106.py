def int_to_mini_roman(n):
    if n < 1000:
        res = []
        for x in range(0, n + 1):
            if x != 0:
                res.append(mini_roman[x])
        res.reverse()
        return ''.join(res)
    else:
        return "Error!"