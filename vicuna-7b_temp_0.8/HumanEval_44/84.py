

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
    # Convert the number to its octal representation
    octal = base * x
    # Split the octal number into its individual digits
    digits = octal // 10
    # Convert each digit to its corresponding decimal digit
    decimal = (octal % 10) + (digits * (base - 10))
    return str(decimal)
