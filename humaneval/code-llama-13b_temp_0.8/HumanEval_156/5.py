
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
    # Convert given int to a string.
    num_str = str(number)

    # Make an empty string to add each letter of the roman numeral to.
    roman_num = ''

    # The length of the number's string representation.
    len_num_str = len(num_str)

    # The index of the current digit under consideration.
    idx = 0

    # Iterate through the string representation of the number,
    # starting at the least significant digit.
    for digit in num_str:
        # The current digit, in integer form.
        current_digit = int(digit)

        # The index of the current digit within the string representation
        # of the number.
        digit_idx = len_num_str - idx - 1

        # If the current digit is non-zero.
        if current_digit != 0:
            # The place value of the current digit.
            place_val = 10 ** digit_idx

            # If the current digit is 1, 5, or 10.
            if current_digit in (1, 5, 10):
                # The letters to add to the roman numeral, depending on the
                # current digit.
                if current_digit == 1:
                    letters = 'i'
                elif current_digit == 5:
                    letters = 'v'
                else:
                    letters = 'x'

                # Add the letters to the roman numeral.
                roman_num += letters * current_digit

            # If the current digit is between 2 and 4 (inclusive),
            # and the digit to the left of it is less than it.
            elif current_digit in range(2, 5) and (
                idx + 1 < len_num_str
                and int(num_str[idx + 1]) < current_digit
            ):
                # If the current digit is 2 or 3.
                if current_digit in (2, 3):
                    # The letters to add to the roman numeral, depending
                    # on the current digit.
                    if current_digit == 2:
                        letters
