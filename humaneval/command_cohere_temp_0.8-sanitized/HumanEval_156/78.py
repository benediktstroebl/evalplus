def int_to_mini_roman(num):
    if num < 1:
        return ""

    res = []
    for i in range(0, len(str(num)) + 1):
        div, mod = divmod(num, 5) if i == 0 else divmod(mod, 5)
        num = div if div > 0 else 1
        res.append(ROMAN_NUM[mod])
        num = str(num)
        if i == 0 and num[-1] == '1':
            res.append(num)
        elif i > 0 and num[-1] == '1':
            res.append(num[0])
        else:
            res.append('x')

    return ''.join(res)
ROMAN_NUM = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}