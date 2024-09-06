

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
    return str(int(x) in {8, 9, 10} and base - 1 or int(x) in {1, 2, 3} and (base - 1) * int(x) + 1 or int(x) in {1, 2} and int(x) + (base - 1) or int(x) in {0} and int(x) * (base - 1) or int(x) in {0, 1} and int(x) * (base - 1) + 1 or int(x) in {0} and int(x) * (base - 1) + 0 or int(x) in {0} and int(x) * (base - 1) + 1 and int(x) < 26 or int(x) in {0} and int(x) * (base - 1) + 1 and int(x) > 25)
