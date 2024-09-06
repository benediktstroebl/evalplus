
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
    roman_numeral = "xxi"
    roman_numerals = ["i", "v", "x", "l", "c", "d", "m", "x", "l", "c", "d", "m", "x", "l", "c", "d", "m"]

    nums = [1,5,10,50,100,500,1000,1000,500,100,50,10,5,1,1,1,1,1]

    i = 0
    while nums[i] > number:
        i += 1

    roman_numerals = roman_numerals[i:]

    roman_numeral = ""
    while number > 0:
        for i in range(len(roman_numerals)):
            if number < nums[i]:
                break
            number -= nums[i]
            roman_numeral += roman_numerals[i]

    return roman_numeral

