def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Swap out numeric values for their roman numeral equivalents
    roman_dict = {1: "i", 5: "v", 10: "x", 50: "l", 100: "c", 500: "d", 1000: "m"}

    roman_num = []
    for i in range(0, n // 1000 + 1):
        value = n - (i * 1000)
        for j in range(0, value // 100 + 1):
            roman_num.append(roman_dict[100])
        value = value % 100
        for j in range(0, value // 50 + 1):
            roman_num.append(roman_dict[50])
        value = value % 50
        for j in range(0, value // 10 + 1):
            roman_num.append(roman_dict[10])
        value = value % 10
        for j in range(0, value // 5 + 1):
            roman_num.append(roman_dict[5])
        value = value % 5
        for j in range(0, value + 1):
            roman_num.append(roman_dict[1])

    return "".join(roman_num)