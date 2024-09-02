
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
    int_to_roman = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    roman_str = ''
    # We can't just do 1000 / 1000000 while number > 0
    # because then we would get stuck on one roman numeral forever.
    # So instead we keep dividing by 1000,
    # then extracting the remainder (mod 1000)
    # and converting that to roman numerals.
    while number > 0:
        # We want to go from highest to lowest roman numerals,
        # so first we divide by the highest powers of 1000,
        # then use the remainder to get the roman numerals for
        # that section.
        roman_str += int_to_roman[1000] * (number // 1000)
        number = number % 1000

        # Now that we have all the roman numerals, we go back and
        # add any additional roman numerals we might need for
        # multiples of 500, 100, 50, 10, or 5.
        if number >= 500:
            roman_str += 'd' * (number // 500)
            number = number % 500

        if number >= 100:
            roman_str += 'c' * (number // 100)
            number = number % 100

        if number >= 50:
            roman_str += 'l' * (number // 50)
            number = number % 50

        if number >= 10:
            roman_str += 'x' * (number // 10)
            number = number % 10

        if number >= 5:
            roman_str += 'v' * (number // 5)
            number = number % 5

        if number >= 1:
            roman_str += 'i'
