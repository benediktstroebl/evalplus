
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

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_string = ''
    prev = None

    for i in sorted(roman_dict.keys(), reverse=True):
        curr = roman_dict[i]
        num = number // curr
        number -= curr * num
        roman_string += num * i

        if prev is not None:
            if curr < prev:
                roman_string += prev * (num - 1)
                number += prev * (num - 1)

        if number == 0:
            break

        prev = curr

    return roman_string.lower()
