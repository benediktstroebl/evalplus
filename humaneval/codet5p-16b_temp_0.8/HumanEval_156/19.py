
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

    roman_numeral_map = (('I', 'V'), ('X', 'L'), ('C', 'D'), ('M', ''))
    thousands, hundreds, tens, units = 1, 0, 0, 0
    result = ''
    while number > 0:
        current_numeral, number = number % 10, number // 10
        if current_numeral == 4:
            tens, units = tens + current_numeral, units + current_numeral
        elif current_numeral == 9:
            tens, units = tens + current_numeral, units + current_numeral
        elif current_numeral >= 5:
            tens, units = tens + current_numeral, units + current_numeral
        elif current_numeral >= 1:
            units = units + current_numeral
        thousands, hundreds, tens, units = tens * 1000 + units * 100 + thousands * 10 + hundreds * 1, hundreds * 1000 + tens * 100 + units * 10 + thousands * 1, tens * 1000 + units * 100 + thousands * 10 + hundreds * 1, units * 1000 + thousands
