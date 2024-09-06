

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

    if not 2 <= base <= 10:
        raise ValueError(f"Invalid base {base}")

    def get_number_digits(num: int):
        result = []
        while num > 0:
            num, remainder = divmod(num, base)
            result.append(remainder)
        return result

    digits = get_number_digits(x)

    return ''.join([str(digit) for digit in digits[::-1]])









































































































































