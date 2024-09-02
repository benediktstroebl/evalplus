
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
    # Phase 1:
    # 1) Create a mapping between our number and its roman equivalent, using
    # a list of tuples.
    # 2) Create a lookup dictionary from that list of tuples
    # 3) Create a list of tuples to loop through, and use each tuple to:
    #    3.1) Determine if the current number is greater than or equal to
    #         the number from the tuple.
    #    3.2) If it is, update our output string with the current letter
    #         corresponding to the number in the tuple.
    #    3.3) Then subtract the number from the tuple from our current number.
    # 4) Return the output string

    # Phase 2:
    # 1) Create a dictionary from a list of tuples
    # 2) Create a list of tuples to loop through, and use each tuple to:
    #    2.1) Determine if the current number is greater than or equal to
    #         the number from the tuple.
    #    2.2) If it is, update our output string with the current letter
    #         corresponding to the number in the tuple.
    #    2.3) Then subtract the number from the tuple from our current number.
    # 3) Return the output string

    # Phase 3:
    # 1) Create a dictionary from a list of tuples
    # 2) Create a list of tuples to loop through, and use each tuple to:
    #    2.1) Determine if the current number is greater than or equal to
    #         the number from the tuple.
    #    2.2) If it is, update our output string with the current letter
    #         corresponding to the number in the tuple.
    #    2.3) Then subtract the number from the tuple from our current number.
    #    2.4) Check if our number is greater than zero, and recursively call
    #         the function if it is.
    # 3) Return the output string
    # 4) Handle an invalid input

    roman_numerals = [
        (1000, 'm'),
        (900, '
