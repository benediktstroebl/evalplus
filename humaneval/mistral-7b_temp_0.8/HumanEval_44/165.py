

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
    def divide(n: int, b: int):
        """Divide n by b."""
        if n == 0:
            return 0
        return n % b + divide(n // b, b)

    def multiply(n: int, b: int):
        """Multiply n by b."""
        if n == 0:
            return 0
        return n * b + multiply(n // b, b)

    def get_digit(n: int, b: int):
        """Find and return digit of n, base b.
        >>> get_digit(8, 10)
        8
        >>> get_digit(8, 3)
        2
        >>> get_digit(8, 2)
        1
        """
        if n == 0:
            return 0
        return get_digit(n // b, b) + n % b

    # divide and multiply are using the same function.
    # divide should work first, then multiply.
    # The result should be divied by 10.
