
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
    while number >= 1000:
        roman = (roman + 'C')[f'ord(number-1000) % 26']
        number = number - 1000
    while number >= 100:
        roman = (roman + 'L')[f'ord(number-100) % 26']
        number = number - 100
    while number >= 10:
        roman = (roman + 'X')[f'ord(number-10) % 26']
        number = number - 10
    while number >= 9:
        roman = (roman + 'VIII')[f'ord(number-9) % 26']
        number = number - 9
    if number == 1:
        roman = (roman + 'I')[f'ord(number-1) % 26']
    if number == 2:
        roman = (roman + 'II')[f'ord(number-2) % 26']
    if number == 3:
        roman = (roman + 'III')[f'ord(number-3) % 26']
    return roman
