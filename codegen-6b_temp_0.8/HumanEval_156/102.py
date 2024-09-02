
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
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000")
    if number < 50:
        return to_roman_dict[number]
    if number < 100:
        ten_numerator = int(number / 10)
        ten_less_numerator = number - ten_numerator * 10
        return to_roman_dict[ten_numerator] + to_roman_dict[ten_less_numerator]
    if number < 500:
        hundred_numerator = int(number / 100)
        hundred_less_numerator = number - hundred_numerator * 100
        return to_roman_dict[hundred_numerator] + 'hundred ' + int_to_mini_roman(hundred_less_numerator)
    if number < 5000:
        thousand_numerator = int(number / 1000)
        thousand_less_numerator = number - thousand_numerator * 1000
        return int_to_mini_roman(thousand_numerator) + 'thousand ' + int_to_mini_roman(thousand_less_numerator)

