
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

    roman_string = ""
    num_map = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbol_map = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    i = 0
    while number > 0:
        while num_map[i] > number:
            i += 1
        roman_string += symbol_map[i]
        number -= num_map[i]
    return roman_string.lower()
