
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
    roman = ''
    digit = number
    while digit > 0:
        if digit % 10 == 1:
            roman += 'I'
        elif digit % 10 == 2:
            roman += 'II'
        elif digit % 10 == 3:
            roman += 'III'
        elif digit % 10 == 4:
            roman += 'IV'
        elif digit % 10 == 5:
            roman += 'V'
        elif digit % 10 == 6:
            roman += 'VI'
        elif digit % 10 == 7:
            roman += 'VII'
        elif digit % 10 == 8:
            roman += 'VIII'
        elif digit % 10 == 9:
            roman += 'IX'
        digit = int(digit / 10)
    return roman
