
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
    roman_numerals = {1: "i", 5: "v", 10: "x"}
    roman_powers = ["", "d", "c", "l", "m", "v", "r"]
    roman_power_count = 0

    while number > 0:
        if number == 5:
            yield "v"
        elif number == 10:
            yield "x"
        elif number < 5:
            for _ in range(number):
                yield roman_numerals[roman_powers[roman_power_count]]
        elif number < 10:
            yield roman_numerals[roman_powers[roman_power_count + 1]]
            roman_power_count += 1
        else:
            yield roman_numerals[roman_powers[roman_power_count]]
            yield roman_numerals[roman_powers[roman_power_count + 1]]
            roman_power_count += 2
        number -= roman_power_count

    return "".join(int_to_mini_roman(number))

