
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman = []
    if number == 0:
        roman.append("I")
    else:
        digit = str(number)
        if digit[-1] >= "A":
            digit = digit[:-1]
        while digit:
            digit_val = ord(digit[0]) - 48
            if digit_val >= 0:
                roman.append(digits_roman[digit_val])
            digit = digit[1:]
        if "I" not in roman:
            roman.append("I")
    return roman[::-1].lower()
