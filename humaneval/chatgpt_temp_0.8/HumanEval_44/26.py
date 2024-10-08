# CANNOT PARSE CODE SNIPPET
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return ''.join(reversed(digits))
