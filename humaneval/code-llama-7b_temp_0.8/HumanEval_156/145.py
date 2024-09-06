
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

    # helper function to convert the thousands place, requires a number 0-3
    def convert_thousands(num):
        switcher = {
            0: '',
            1: 'm',
            2: 'mm',
            3: 'mmm',
        }
        return switcher.get(num)

    # helper function to convert the hundreds place, requires a number 0-3
    def convert_hundreds(num):
        switcher = {
            0: '',
            1: 'c',
            2: 'cc',
            3: 'ccc',
        }
        return switcher.get(num)

    # helper function to convert the tens place, requires a number 0-3
    def convert_tens(num):
        switcher = {
            0: '',
            1: 'x',
            2: 'xx',
            3: 'xxx',
        }
        return switcher.get(num)

    # helper function to convert the ones place, requires a number 0-3
    def convert_ones(num):
        switcher = {
            0: '',
            1: 'i',
            2: 'ii',
            3: 'iii',
        }
        return switcher.get(num)

    # use helper functions to find the places for ones, tens, hundreds, thousands
    thousands = convert_thousands(number//1000)
    hundreds = convert_hundreds((number%1000)//100)
    tens = convert_tens(((number%1000)%100)//10)
    ones = convert_ones(((number%1000)%100)%10)

    # return the concatenation of the values
    return thousands + hundreds + tens + ones
