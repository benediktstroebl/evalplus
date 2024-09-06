
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
    roman = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }
    num_dict = {}
    for i in range(1, 1000, 500):
        num_dict[i] = roman[i] + roman[i+1] + roman[i+2]

    num_dict[999] = 'cm'
    num_dict[998] = 'cxc'
    num_dict[997] = 'cxci'
    num_dict[996] = 'cxcc'
    num_dict[995] = 'cxcl'
    num_dict[994] = 'cxcl'
    num_dict[993] = 'cxci'
    num_dict[992] = 'cxc'
    num_dict[991] = 'cxc'
    
