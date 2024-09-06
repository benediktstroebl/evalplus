
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
    int_to_roman = {
        1 : "i",
        5 : "v",
        10 : "x",
        50 : "l",
        100 : "c",
        500 : "d",
        1000 : "m"
    }
    num_to_roman = ""
    while number > 0:
        for num in sorted(int_to_roman.keys(), reverse=True):
            if number >= num:
                number -= num
                num_to_roman += int_to_roman[num]
    return num_to_roman

