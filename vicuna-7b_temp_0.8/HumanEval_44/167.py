

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
    # convert each digit of the number to its corresponding number in the new base
    number = str(x)
    converted_number = ""
    for i, digit in enumerate(number):
        if i % base == 0:
            converted_number += "0"
        converted_number += str(digit * (int(base) - i % base))

    return converted_number
