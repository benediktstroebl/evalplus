
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
    roman_numerals = (
        ('m', 1000), ('cm', 900), ('d', 500), ('c', 100), ('xc', 90), ('l', 50),
        ('x', 10), ('ix', 9), ('v', 5), ('iv', 4), ('i', 1)
    )

    if number <= 0 or number > 1000:
        raise ValueError('Number out of range (1..1000)')

    output = []

    for (letter, number_of_times_letter_appears) in roman_numerals:

        while number_of_times_letter_appears >= number:
            output.append(letter)
            number -= number_of_times_letter_appears

    return ''.join(output)
