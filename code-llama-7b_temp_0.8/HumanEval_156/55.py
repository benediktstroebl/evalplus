
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

    #
    # IMPLEMENT YOUR SOLUTION HERE
    #
    roman_dict = {1:'i', 4:'iv', 5:'v', 9:'ix', 10:'x', 40:'xl', 50:'l', 90:'xc', 100:'c', 400:'cd', 500:'d', 900:'cm', 1000:'m'}
    num = number
    roman_num = ''
    while num > 0:
        for key in roman_dict:
            if num >= key:
                roman_num += roman_dict[key]
                num -= key
    return roman_num.lower()
    
