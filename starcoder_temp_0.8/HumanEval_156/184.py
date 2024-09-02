
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
    # The Roman Numeral List
    roman_nums = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                  (5, "V"), (4, "IV"), (1, "I")]
    # We will first need to find the most frequent divisor
    # so that the conversion is as accurate as possible
    divisor = 1
    for rnum in roman_nums:
        if number >= rnum[0]:
            divisor = rnum[0]
    # We will then write the roman numeral string
    roman = ''
    while divisor > 0:
        quotient, remainder = divmod(number, divisor)
        roman += roman_nums[roman_nums.index((divisor, ''))][1] * quotient
        number = remainder
        divisor /= 10
    return roman
