
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
    if number < 1:
        return ''
    if number <= 10:
        return roman[number-1]
    if number < 40:
        return roman[number//10-1] + roman[number % 10 - 1]
    if number < 50:
        return roman[number//10-1] + roman[0]
    if number < 100:
        return roman[number//10-1] + roman[1]
    if number < 400:
        return roman[number//100 - 1] + roman[0] + roman[number % 100//10 - 1] + roman[number % 10]
    if number < 500:
        return roman[number//100 - 1] + roman[0] + roman[1] + roman[number % 10]
    if number < 900:
        return roman[number//100 - 1] + roman[1] + roman[number % 100//10 - 1] + roman[number % 10]
    if number < 1000:
        return roman[number//100 - 1] + roman[1] + roman[0] + roman[number % 100]
    
    
