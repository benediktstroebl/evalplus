def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Correspondence between Arabic and Roman numerals
    arabic = ["i", "v", "x", "l", "c", "d", "m"]
    roman = ["i", "iv", "ix", "xl", "xc", "xd", "xm"]

    result = []
    while n > 0:
        for arabic_num in range(0, n // 5 + 1):
            result.append(arabic[arabic_num])
            n -= 5 * arabic_num
        if n > 0:
            result.append(arabic[n % 5])
    result.reverse()

    return "".join(roman[i] for i in result)