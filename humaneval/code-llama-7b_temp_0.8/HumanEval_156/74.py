
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
    num_dict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    num_dict_values = list(num_dict.values())
    num_dict_keys = list(num_dict.keys())
    return_val = ""
    if number <= 0 or number >= 1000:
        return "Not a valid roman numeral"
    else:
        for i in num_dict_keys:
            while number >= i:
                if number > 1000:
                    number = number - i
                    return_val = return_val + num_dict_values[num_dict_keys.index(i)]
                    return_val = return_val + num_dict_values[num_dict_keys.index(i)]
                else:
                    number = number - i
                    return_val = return_val + num_dict_values[num_dict_keys.index(i)]
    return return_val.lower()
