def int_to_mini_roman(n):
    if n < 1:
        return ""

    # equivalencies and reductions
    roman = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "l",
        50: "l",
        90: "xl",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m"
    }
    result = []

    while n > 0:
        temp = roman[n]
        if len(temp) > 1:
            result.append(temp)
        else:
            result.append(temp[0])
        n -= roman[n]

    return ''.join(result)