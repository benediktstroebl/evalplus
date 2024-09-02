
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError('int_to_mini_roman() only takes positive integers in the range 1 <= num <= 1000')
    
    num_repr = ''
    digits = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    numeral = [('', '', '', 'm', 'c', 'd', '', '', '', ''),
               ('', '', '', 'x', 'l', 'x', '', '', '', ''),
               ('', '', '', 'i', 'v', 'i', '', '', '', ''),
               ('', '', '', '', '', '', '', '', '', ''),
               ('', '', '', '', '', '', '', '', '', ''),
               ('', '', '', '', '', '', '', '', '', '')]
    
    for weight in digits:
        if number >= weight:
            num_repr += numeral[weight - 1][0]
            number -= weight
    
    return num_repr.lower()
    
