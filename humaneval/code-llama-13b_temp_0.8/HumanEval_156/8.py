
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
    # NOTE: This solution does not handle the edge case of 0.
    # Leave that to the caller.

    # A mapping of powers of 10 to their roman equivalent
    # NOTE: The range does not include the stop value.
    # Hence, the range is from 0 to 1000 with a step of 100.
    mapping = dict()
    mapping[100] = 'c'
    mapping[500] = 'd'
    mapping[1000] = 'm'

    # The list to store the roman numerals
    roman_numerals = list()

    # The number of each power of 10 that is taken from the number.
    count = 0
    while number > 0:
        # The power of 10 to take from the number
        power = 10 ** count

        # If the number has more than or equal to the power,
        # then add the corresponding roman equivalent to the list.
        if number // power >= 5:
            # The number's count for the current power of 10
            temp = number // power

            # The roman equivalent for the current power of 10
            roman_equiv = mapping[power]

            # If the current power of 10 is 100,
            # then the roman equivalent is repeated temp times
            if power == 100:
                roman_equiv *= temp

            # Add the equivalent to the list.
            roman_numerals.append(roman_equiv)

            # Subtract the equivalent's value from the number
            number -= temp * power

        # If the number has less than 5 powers of 10,
        # then add the corresponding roman equivalent to the list.
        elif 1 <= number // power < 5:
            # The number's count for the current power of 10
            temp = number // power

            # The roman equivalent for the current power of 10
            roman_equiv = mapping[power]

            # If the current power of 10 is 100,
            # then the roman equivalent is repeated temp times
            if power ==
