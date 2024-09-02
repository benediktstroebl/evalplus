
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
    int_to_roman = (
        '', 'M', 'CM', 'D', 'CD', 'DCCC', 'DCC', 'DC', 'MCD', 'MC', 'MCC',
        'MCM', 'MM', 'MMM'
    )

    # NOTE: Python integer numbers cannot be negative
    assert (number >= 0) and (number <= 1000)

    # NOTE: Check if the given number is less than 0
    if number < 0:
        raise ValueError('The number is less than 0')

    # NOTE: Check if the given number is less than 1000
    if number > 1000:
        raise ValueError('The number is larger than 1000')

    # NOTE: Check if the given number is 100
    if number == 100:
        return 'C'

    # NOTE: Check if the given number is below 100
    if number < 100:

        # NOTE: Obtain the remainder
        remainder = number % 10

        # NOTE: Return the index of the remainder
        return int_to_roman[remainder]

    # NOTE: Number is larger than 100
    unconfirmed_numbers = range(1, 10)[::-1] + ['A', 'B', 'C', 'D', 'E', 'F']

    # NOTE: Loop through the numbers of the unconfirmed numbers
    for index in range(0, len(unconfirmed_numbers)):

        # NOTE: Check if the given number is equal to the current unconfirmed number
        if number == unconfirmed_numbers[index]:

            # NOTE: Return the index of the current unconfirmed number
            return int_to_roman[index]

