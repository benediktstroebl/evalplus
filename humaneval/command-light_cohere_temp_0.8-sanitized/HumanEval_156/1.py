def int_to_mini_roman(number):
    """
    Converts a positive integer to its roman numeral equivalent and returns it in lowercase.
    1 <= num <= 1000
   
    Examples:
        >>> int_to_mini_roman(19) == 'xix'
        >>> int_to_mini_roman(152) == 'clii'
        >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    if number <= 100:
        return 'one' + number
    elif number >= 4999 and number <= 5999:
        return 'five' + int_to_mini_roman(number - 4000)
    elif number >= 500 and number <= 599:
        return 'five' + 'xx' + int_to_mini_roman(number - 500)
    elif number >= 600 and number <= 7999:
        return 'six' + 'xx' + int_to_mini_roman(number - 600)
    elif number >= 800 and number <= 879:
        return 'eight' + 'xx' + int_to_mini_roman(number - 800)
    elif number >= 900 and number <= 999:
        return 'nine' + 'xx'
    else:
        return 'three' + int_to_mini_roman(number - 1000)