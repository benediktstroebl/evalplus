```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    symbols = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]
    tens = ["", "x", "l", "c", "d", "m"]
    hundreds = ["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]

    roman_num = []

    # Handle 1 to 9
    for i in range(1, n + 1):
        roman_num.append(symbols[i - 1])

    # Handle 10 to 99
    for i in range(1, n // 10 + 1):
        roman_num.append(tens[i] + symbols[n // 10 - i])

    # Handle 100 to 999
    for i in range(1, n // 100 + 1):
        roman_num.append(hundreds[i] + tens[n // 100 - i] + symbols[n % 100 - (i * 10)])

    return "".join(roman_num).lower()
```

This approach uses a nested loop structure for converting the integer input into a Roman numeral string. It utilizes separate lists of Roman numerals, tens, and hundreds for efficient manipulation and aggregation of the string. The result is a Roman numeral string in lowercase, as specified by the prompt's requirements.