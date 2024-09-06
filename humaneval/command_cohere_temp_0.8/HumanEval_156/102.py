```python
def int_to_mini_roman(num):
    mini_roman = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
    tens = [None, 'x', 'l', 'c', 'd', 'm']
    hundreds = [None, 'c', 'cc', 'd', 'dd', 'm', 'mm']

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
            print(f"Error processing digit {digit}")
            return None

    roman_num = [''] * int(num / 1000) + roman_num + [''] * (1000 - int(num))

    curr = num // 10
    for digit in roman_num:
        if curr >= 1 and curr <= 3:
            roman_num[len(roman_num) - 1] += tens[curr - 1]
        elif curr >= 4 and curr <= 7:
            roman_num[len(roman_num) - 1] += hundreds[curr - 4]
        curr = num % 10

    return ''.join(roman_num).lower()
```

The `int_to_mini_roman` function accepts a positive integer and converts it to its mini roman numeral representation as a string, with the restrictions provided in the prompt. It uses lists to map digits to roman numerals and constructs the result incrementally, following the roman numeral rules. The thousands place is handled by adding an empty string to split the roman numeral into groups of three, as specified in the problem. The final result is converted to lowercase.