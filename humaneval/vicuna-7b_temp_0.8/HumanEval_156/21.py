
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
    numeral_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    numeral_map.update({
        i: str(i) + 'I' for i in range(201, 223)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(224, 236)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(237, 245)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(246, 256)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(257, 258)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(257, 258)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(257, 258)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(257, 258)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(257, 258)
    })

    numeral_map.update({
        i: str(i) + 'I' for i in range(257, 258)
    })

    numeral
