
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

    # The numbers we will be working with
    ones = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # The roman numeral equivalents
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    # The result to return
    result = ""

    # Go through the numbers list, and while our number is larger than the current
    # number, add the roman number to the result.
    for i in range(len(ones)):
        while number >= ones[i]:
            result += romans[i]
            number -= ones[i]
    return result.lower()

