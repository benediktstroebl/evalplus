
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
    if number >= 1000:
        roman = 'M'*(number//1000)
        number -= 1000*(number//1000)
    if number >= 900:
        roman += 'CM'
        number -= 900
    if number >= 500:
        roman += 'D'
        number -= 500
    if number >= 400:
        roman += 'CD'
        number -= 400
    if number >= 100:
        roman += 'C'*(number//100)
        number -= 100*(number//100)
    if number >= 90:
        roman += 'XC'
        number -= 90
    if number >= 50:
        roman += 'L'
        number -= 50
    if number >= 40:
        roman += 'XL'
        number -= 40
    if number >= 10:
        roman += 'X'*(number//10)
        number -= 10*(number//10)
    if number >= 9:
        roman += 'IX'
        number -= 9
    if number >= 5:
        roman += 'V'
        number -= 5
    if number >= 4:
        roman += 'IV'
        number -= 4
    roman += 'I'*number
    return roman

