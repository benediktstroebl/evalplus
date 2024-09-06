
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
    # convert integer to string
    number = str(number)

    # initialize place value
    place_value = 1

    # initialize empty string
    roman = ''

    # iterate through number
    for i in range(len(number)):
        # fetch current digit as string
        digit = number[len(number) - i - 1]

        # convert current digit to integer
        digit = int(digit)

        # if digit is zero
        if digit == 0:
            pass

        # if digit is 1
        elif digit == 1:
            # add its symbol to the string
            roman = unichr(8704 + place_value) + roman

        # if digit is 2
        elif digit == 2:
            # add its symbol to the string twice
            roman = unichr(8704 + place_value) * 2 + roman

        # if digit is 3
        elif digit == 3:
            # add its symbol to the string three times
            roman = unichr(8704 + place_value) * 3 + roman

        # if digit is 4
        elif digit == 4:
            # add its symbol to the string
            roman = unichr(8704 + place_value) + unichr(8704 + place_value * 5) + roman

        # if digit is 5
        elif digit == 5:
            # add its symbol to the string
            roman = unichr(8704 + place_value * 5) + roman

        # if digit is 6
        elif digit == 6:
            # add its symbol to the string
            roman = unichr(8704 + place_value * 5) + unichr(8704 + place_value) + roman

        # if digit is 7
        elif digit == 7:
            # add its symbol to the string
            roman = unichr(8704 + place_value) * 3 + unichr(8704 + place_value * 5) + roman

        # if digit is 8
        elif
