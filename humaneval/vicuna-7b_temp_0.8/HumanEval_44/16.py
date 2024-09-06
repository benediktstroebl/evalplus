

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Convert the base number to its corresponding ASCII character
    ascii_map = {
        1: '0',
        2: '1',
        3: '2',
        4: '3',
        5: '4',
        6: '5',
        7: '6',
        8: '7',
        9: '8',
        10: '9',
        11: 'A',
        12: 'B',
        13: 'C',
        14: 'D',
        15: 'E',
        16: 'F',
    }
    ascii_map[base] = chr(ord(ascii_map[base]) + 8 - base)

    # Convert the input number to base
    converted_number = 0
    if base > 0:
        while x > 0:
            if x % base == 0:
                converted_number = converted_number * base + (x // base)
            x //= base
        converted_number = int(converted_number)
    else:
        while x > 0:
            if x % base == 0:
                converted_number = converted_number * base + (x // base)
            x //= base
        converted_number = int(converted_number)

    # Get the ASCII value of the converted number
    ascii_value = chr(ord(str(converted_number)))

    # Get the ASCII value of the base
    base_value = ascii_map.get(base, '0')

    # Get the ASCII value of the separator
    separator = '0' if base < 10 else chr(ord('A') + (base - 1) // 26)

    # Get the ASCII value of the converted number with separator
    string_representation = ascii_value + separator + base_value

    return string_representation
