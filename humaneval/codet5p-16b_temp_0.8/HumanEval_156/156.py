
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

    
    numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    numerals = [x.lower() for x in numerals]
    roman = ""
    
    while number > 0:
        for numeral in numerals:
            if number >= numerals.index(numeral):
                roman += numeral
                number -= numerals.index(numeral)
    
    return roman
