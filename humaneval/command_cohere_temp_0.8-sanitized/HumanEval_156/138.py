def int_to_mini_roman(num):
    mini_roman = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    tens = ['x', 'l', 'c', 'd', 'm']
    hundreds = ['c', 'cd', 'd', 'dm', 'm']

    roman_num = []

    for digit in str(num):
        if digit == '1':
            roman_num.append(mini_roman[0])
        elif digit == '2':
            roman_num.append(mini_roman[1])
        elif digit == '3':
            roman_num.append(mini_roman[2])
        elif digit == '4':
            roman_num.append(mini_roman[3])
        elif digit == '5':
            roman_num.append(mini_roman[4])
        elif digit == '6':
            roman_num.append(mini_roman[5])
        elif digit == '7':
            roman_num.append(mini_roman[6])
        elif digit == '8':
            roman_num.append(mini_roman[7])
        elif digit == '9':
            roman_num.append(mini_roman[8])
        elif digit == '0':
            pass
        else:
            roman_num.append(str(digit))

    roman_str = ''
    i = 0
    while i < len(roman_num):
        if i == len(roman_num) - 1:
            roman_str += roman_num[i]
        elif roman_num[i] == 'm' and num % 1000 >= 500:
            roman_str += 'mil'
        elif roman_num[i] == 'm' and num % 1000 < 500:
            roman_str += 'min'
        elif roman_num[i] == 'c' or roman_num[i] == 'd':
            if i < len(roman_num) - 1 and (roman_num[i + 1] == 'c' or roman_num[i + 1] == 'd'):
                roman_str += hundreds[num // 100 - 1]
                i += 1
            else:
                roman_str += roman_num[i]
        else:
            roman_str += tens[num // 10 - 1]
        i += 1

    return roman_str.lower()