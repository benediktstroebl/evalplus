
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
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    roman_list = []
    # Create a list with the keys of the dictionary,
    # in reverse order of their values.
    # For example, when the number is 19,
    # we will get ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    # in this order.
    roman_keys = list(reversed(roman_dict.keys()))
    # In this example,
    # the list 'roman_keys' is
    # ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    # 'roman_list' is an empty list
    for key in roman_keys:
        # Loop through the list 'roman_keys'
        # from beginning to end
        # In this example,
        # the first iteration is when 'key
