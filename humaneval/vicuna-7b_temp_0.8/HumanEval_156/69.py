
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
    if number > 1000:
        return "M" + number % 1000 + "D"
    if number >= 100 and number not in (100, 200, 300, 400, 500, 600, 700, 800, 900):
        return "C" + "V"[number > 900]
    if number >= 50 and number not in (50, 100, 200, 300, 400, 500, 600, 700, 800, 900):
        return "X" + "V"[number > 900]
    if number == 500:
        return "D"
    if number == 400:
        return "CD"
    if number == 300:
        return "C" + "D"
    if number == 200:
        return "II"
    if number == 100:
        return "I"
    if number == 90:
        return "IX"
    if number == 80:
        return "VIII"
    if number == 70:
        return "VII"
    if number == 60:
        return "VI"
    if number == 50:
        return "V"
    if number == 40:
        return "IV"
    if number == 30:
        return "III"
    if number == 20:
        return "II"
    if number == 10:
        return "I"
    return "0"
