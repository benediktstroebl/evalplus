
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
    # check input
    if type(number) is not int or number < 1 or number > 1000:
        raise ValueError

    # initialize an array of roman numerals
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""

    # loop through the numbers and subtract the largest number
    # repeatedly from the number to get the appropriate roman numeral
    for i in range(len(numbers)):
        while number >= numbers[i]:
            result += roman[i]
            number -= numbers[i]
    return result
