
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
    # Use a dictionary to store the API of roman numerals for later
    # use.
    ROMAN_NUMERAL_DICT = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }

    # Use a queue to crawl the roman numeral value upward.
    # The value of the numeral is the first element in the queue.
    roman_numeral_queue = deque([])

    # Use an integer to keep track of the number of subtraction operations done to
    # reach the given input value.
    num_subtraction_ops = 0
    # Use a boolean to track whether or not the roman numeral value has been
    # found.
    found_roman_numeral = False

    # For the input value, keep crawling the roman numeral value upward to reach
    # its upper limit.
    while number > 0:
        # Find the roman numeral value that matches the input value.
        for key, value in ROMAN_NUMERAL_DICT.items():
            if number - key <= 0:
                num_subtraction_ops += len(value)
                roman_numeral = value
                found_roman_numeral = True
                break
        # If no roman numeral matches the input value, then the input value is
        # greater than the limit of the Roman numeral, so return ''.
        if not found_roman_numeral:
            return ''
        # If the input value is not 0, pop the roman numeral value from the queue
        # and add it to the end of the roman numeral value.
        if number != 0:
            roman_numeral_queue.append(roman_numeral)
            number -= key
        # If the input value is 0, then we have reached the final roman numeral
        # value, so add the entire roman numeral value to the end of