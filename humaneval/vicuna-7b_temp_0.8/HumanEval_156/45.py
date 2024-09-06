
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
    roman_chars = "I IX V M C D T Q U W E O R I X L C S D T Q U A I I I I V I I I I I X I I I I I"
    result = ""
    for i in range(10):
        if number >= 4000:
            result += roman_chars[int(number/1000)]
            number %= 1000
        elif number >= 1000:
            result += roman_chars[int(number/1000) - 4]
            number %= 1000
        elif number >= 100:
            result += roman_chars[int(number/100)]
            number %= 100
        elif number >= 10:
            result += roman_chars[int(number/10)]
            number %= 10
        elif number > 0:
            result += roman_chars[int(number)]
    return result.lower()
