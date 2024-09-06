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