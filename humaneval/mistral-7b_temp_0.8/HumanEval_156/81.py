
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
    if number > 1000:
        raise ValueError("number must be less than or equal to 1000")
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
             90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
             5: 'V', 4: 'IV', 1: 'I'}
    result = ""
    for k, v in roman.items():
        if number < k:
            continue
        elif number < (k * 10):
            result += (v * (number // k))
            number = (number % k)
        else:
            result += (v * 10)
    return result

