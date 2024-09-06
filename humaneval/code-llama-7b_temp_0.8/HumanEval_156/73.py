
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
    if number <= 0:
        raise ValueError("Please enter a positive integer.")
    elif number >= 1000:
        raise ValueError("Please enter an integer less than 1000.")
    else:
        roman_num = ""
        if number >= 1000:
            roman_num += "m"*int(number/1000)
            number %= 1000
        if number >= 100:
            roman_num += "c"*int(number/100)
            number %= 100
            if number >= 50:
                roman_num += "d"
                number %= 50
            elif number >= 40:
                roman_num += "x"
                number %= 40
                roman_num += "v"
                number %= 10
            else:
                roman_num += "c"
                number %= 10
        if number >= 10:
            roman_num += "x"*int(number/10)
            number %= 10
            if number >= 5:
                roman_num += "v"
                number %= 5
            elif number >= 4:
                roman_num += "i"
                number %= 4
            else:
                roman_num += "x"
                number %= 1
        if number >= 1:
            roman_num += "i"*int(number)
    return roman_num
