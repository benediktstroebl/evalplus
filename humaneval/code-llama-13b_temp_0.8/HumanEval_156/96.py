
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
    # Map to make lookup more efficient
    numeral_map = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    # Helper function
    def get_roman_digit(n, base):
        """
        Gets the roman numeral representation of a single digit
        """
        roman_digit = ""
        if n == 0:
            return roman_digit
        if n < 4:
            roman_digit = numeral_map[base] * n
        elif n == 4:
            roman_digit = numeral_map[base] + numeral_map[base * 5]
        elif n < 9:
            roman_digit = numeral_map[base * 5] + (numeral_map[base] * (n - 5))
        else:  # n == 9
            roman_digit = numeral_map[base] + numeral_map[base * 10]
        return roman_digit

    def int_to_roman(num):
        """
        Converts a positive integer to its roman numeral equivalent
        """
        if num == 0:
            return ""
        roman_numerals = ""
        base_values = [1000, 100, 10, 1]
        for base in base_values:
            roman_numerals += get_roman_digit(num // base, base)
            num %= base
        return roman_numerals

    # Split the number into individual digits
    digits = [int(i) for i in str(number)]

    # Convert each digit into its roman equivalent, and concatenate them
    roman_numeral = ""
    for digit in digits:
        roman_numeral += int_to_roman(digit)

    return roman_numeral.lower()

