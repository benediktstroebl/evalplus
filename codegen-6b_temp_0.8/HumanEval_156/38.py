
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
    if (number > 1000 or number < 1):
        raise ValueError("Invalid number")
    digits = []
    while number > 0:
        digit = number % 10
        if digit == 1:
            digits.append("i")
        elif digit == 5:
            digits.append("v")
        elif digit == 10:
            digits.append("x")
        elif digit == 50:
            digits.append("l")
        elif digit == 100:
            digits.append("c")
        elif digit == 500:
            digits.append("d")
        elif digit == 1000:
            digits.append("m")
        elif digit == 4:
            digits.append("iv")
        elif digit == 9:
            digits.append("ix")
        elif digit == 5:
            digits.append("vix")
        elif digit == 10:
            digits.append("xix")
        elif digit == 50:
            digits.append("lx")
        elif digit == 100:
            digits.append("cx")
        elif digit == 500:
            digits.append("cd")
        elif digit == 1000:
            digits.append("m")
        number = number - digit
        number = number / 10
    digits.reverse()
    return "".join(digits)

