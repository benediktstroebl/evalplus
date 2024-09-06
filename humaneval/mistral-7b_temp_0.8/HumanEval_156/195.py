
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
    mapping = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    mapping_inverted = {v: k for k, v in mapping.items()}
    mapping_inverted_ord = {v: ord(k) for k, v in mapping_inverted.items()}

    n = number
    roman = ""
    for key, value in sorted(mapping_inverted_ord.items(), reverse=True):
        while n >= value:
            roman += mapping_inverted[key]
            n -= value
    return roman

