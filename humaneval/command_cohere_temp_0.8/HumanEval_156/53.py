```python
def int_to_mini_roman(num):
    mini_roman = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    tens = ['x', 'l', 'c', 'd', 'm']
    hundreds = ['c', 'cc', 'cd', 'd', 'dc', 'cm']

    result = []
    while num > 0:
        remainder = num % 10
        if remainder == 0:
            result.extend(hundreds[(num // 100) - 1])
            break
        else:
            result.extend(mini_roman[remnant - 1])
            result.append(tens[num // 10 % 10])
            num //= 10

    return ''.join(result).lower()
```

This code uses a list of lists to map each integer value to its mini-roman numeral representation. The tens and hundreds lists convert the values between 1 and 10 and 10 and 100, respectively, to their mini-roman numeral representations. The code then uses a while loop to convert the value of `num` to its mini-roman representation, by dividing it by 10 and using the remainder operator to determine which numeral to use. Finally, the code lowers the case of the roman numeral so that the output is a string consistent with the requested format.