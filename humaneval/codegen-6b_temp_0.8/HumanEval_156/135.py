
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
    roman_numerals = list(
        "xmxcviix cclxvi clii cllxvi clxvii cmxcvi cmii cmmxvi cmlxvii cmivx cccxvii ccvxvii ccixvii cchxvii cdjxvii dcixvii dccxviidd cdxixii dcdxviisc dcmxviisc dcmivxix ddcxvii dcdxvix dcmivii dmmxvii dmlxvii dmcivii dmivxix dmivii dmmivii".split()
    )
    r = ""
    while number > 0:
        for i, roman in enumerate(roman_numerals):
            if number >= roman_numerals[i]:
                r += roman_numerals[i]
                number -= roman_numerals[i]
    return r.lower()

