
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
    roman_dict = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }
    roman_numerals = []
    i = 1000
    while number != 0:
        count = number // i
        if count == 0:
            i = i // 10
        else:
            number = number - count * i
            if i in roman_dict:
                if i > count:
                    roman_numerals.append(roman_dict[i] * count)
                else:
                    if count in roman_dict:
                        roman_numerals.append(roman_dict[count])
                    else:
                        # for numbers > 1000
                        first_roman = roman_dict[i]
                        second_roman = roman_dict[count - i]
                        roman_numerals.append(first_roman + second_roman)

    return ''.join(roman_numerals)

