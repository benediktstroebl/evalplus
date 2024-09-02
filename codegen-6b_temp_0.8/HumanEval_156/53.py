
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
    ROMANS = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    result = ""
    for i in range(1, number+1):
        digit = number // i   # quotient of the number i and the number
        # stored in the variable digit.
        if digit < 4:  # append the roman numeral to result
            result = ROMANS[digit] + result
        elif digit >= 4 and digit < 9:
            result = ROMANS[digit] + result
        elif digit == 9:
            result = ROMANS[digit] + result
            result = ROMANS[10] + result
        number %= i
    return result

