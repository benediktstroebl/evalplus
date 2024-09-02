
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
    roman = ""
    rem = number
    while rem != 0:
        digit = rem % 1000
        roman = f"{roman}{digit}{int_to_roman(digit)}}"[2:] if digit > 0 else f"{roman}{int_to_roman(abs(digit))}}" if abs(digit) < 10 else f"{roman}{int_to_roman(digit) + 1000}"
        rem = rem // 1000
    return roman
