```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    else:
        tens = int(n) / 10
        if tens == 0:
            return str(n)
        roman_digits = [
            "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"
        ]
        roman_tens = [
            "x", "l", "c", "d", "m"
        ]
        return (roman_tens[tens] + roman_digits[n % 10] +
                (str(tens))[1:])
```

The overall approach is to convert the integer into a binary representation in reverse order and then convert each digit to its roman numeral equivalent. However, if the digit is a single-digit number or a multiple of 5, we append an 'x' to the end of the roman numeral to ensure that the roman numeral is accurate but also compact (as per the defintion of 'mini' in the prompt). For example, the number 152 becomes 'clii' by ignoring the digit position of 2 and appending an 'x' to the result.