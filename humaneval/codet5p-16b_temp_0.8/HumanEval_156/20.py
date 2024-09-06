
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

    if type(number)!= int:
        raise TypeError("Input must be an integer.")
    if number < 1 or number > 1000:
        raise ValueError("Input must be between 1 and 1000.")

    mini_roman = ""
    num_to_roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

    for key in num_to_roman:
        while number >= key:
            mini_roman += num_to_roman[key]
            number -= key
    return mini_roman.lower()
