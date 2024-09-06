
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
    if number < 1 or number > 1000:
        raise ValueError("Number out of range")

    # These are the roman symbols used. Note that in the full roman alphabet,
    # there are lowercase letters too (like `M`, `D`, `L` and `V`).
    roman_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    # This dictionary stores the corresponding integer values of each symbol.
    # Note that in the full roman alphabet, `M`, `D`, `L` and `V` have a
    # higher integer value than those.
    roman_symbol_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # To store the roman numeral equivalent.
    roman_numeral = ""

    # Traverse through the digits in the number.
    # Note that we are starting from the ones place and going up to the
    # thousands place.
    digit_place = 0
    while number > 0:
        current_digit = number % 10

        # If the current digit is zero, don't do anything.
        if current_digit == 0:
            digit_place += 1
            number = number // 10
            continue

        # If the current digit is 4 or 9, we will have to add two symbols to
        # represent them.
        if current_digit == 4 or current_digit == 9:
            # Get the symbol corresponding to the current digit.
            current_symbol = roman_symbols[digit_place]
            # Add one more of this symbol to the roman numeral.
            roman_numeral += current_symbol * 2
        # If the current digit is between 1 and 3, just add the symbol.
        elif current_digit == 1 or current_digit == 2 or current_digit == 3:
            # Get the symbol corresponding to the current digit.
            current
