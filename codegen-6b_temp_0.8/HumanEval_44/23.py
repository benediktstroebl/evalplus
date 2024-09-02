

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
    if x < 0:
        raise ValueError("input number cannot be negative")
    digits = []
    while x != 0:
        digits.append(int(x % 10))
        x = x // 10
    if base < 2 or base > 10:
        raise ValueError("base must be between two and ten")
    s = ""
    while len(digits) != 0:
        digit = digits.pop()
        if digit < 10:
            s += str(digit)
        elif digit == 10:
            s += "A"
        elif digit == 11:
            s += "B"
        elif digit == 12:
            s += "C"
        elif digit == 13:
            s += "D"
        elif digit == 14:
            s += "E"
        elif digit == 15:
            s += "F"
    return s[::-1]

