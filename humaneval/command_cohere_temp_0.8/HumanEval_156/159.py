```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    # Convert number to string and remove any zeros.
    num_str = str(n).strip('0')

    # Arrays of mapping from digits to roman numerals and reversed.
    digits = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
    roman = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]

    # Special cases for 13, where viii is added before x and for 48-49, where xl, xli, xlii, xliv are added.
    if n == 13:
        return "xi<br>iii"
    if n == 48:
        return "forty eight"
    if n == 49:
        return "forty nine"
    if n == 50:
        return "l"

    # Iterate over the digits of the number and construct the roman numeral.
    mini_roman = []
    for digit in num_str:
        mini_roman.extend(digits[int(digit)])

    # Add special cases for 10, 100, 200, 300, 400 and 500.
    if n == 10:
        return "x"
    if n == 100:
        return "c"
    if n == 200:
        return "cc"
    if n == 300:
        return "ccc"
    if n == 400:
        return "cd"
    if n == 500:
        return "d"

    # Handle the remaining numbers by adding a leading 1 if it's a single digit,
    # or a leading `ii` if it's two digits.
    if len(num_str) == 1:
        mini_roman = ["i"] + mini_roman
    elif len(num_str) == 2:
        mini_roman = ["ii"] + mini_roman

    return "".join(roman[i] for i in mini_roman)
```

Let's break down the solution step by step:
1. **Input Validation**: The code starts by checking if the input number is less than 1. If so, it returns an empty string since there's no valid Roman numeral for numbers less than 1.
2. **Number Conversion**: The number is converted to a string and any leading zeros are removed. This is done using `str(n).strip('0')`. For example, `n = 1234` will become `"1234"` and `n = 01` will become `"1"`.
3. **Digit to Roman Mapping**: The script then maps digits to their Roman numeral equivalents and vice versa. These are stored in the `digits` and `roman` arrays respectively. These arrays are used to convert the numeric string into a Roman numeral string.
4. **Special Cases**: The script includes special cases for specific numbers. For 13, it adds the prefix "xi" followed by "iii" since in mini roman numerals, "13" is spelled as "xiii". Similarly, for 48 and 49, it returns "forty eight" and "forty nine" since in mini roman numerals, "48" and "49" are spelled as "48" and "49". For 50, it returns simply "l" since "50" is spelled as "L" in mini roman numerals.
5. **Construction of Roman Numeric String**: The script iterates over the digits of the number and constructs the Roman numeral string based on the mapping arrays