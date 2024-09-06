def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for i in range(1, 1000):
        if n >= i:
            num = str(i)
            roman = ROMAN_NUM[i]
            idx = len(roman) - 1
            while num > 0 and idx >= 0:
                res.append(roman[idx])
                num -= roman[idx]
                idx -= 1
            if num > 0:
                res.append(num)
            n -= i

    return ''.join(res)
ROMAN_NUM = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}