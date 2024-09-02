

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
    # handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    convertString = "0123456789abcdefghijklmnopqrstuvwxyz"
    stack = Stack()

    while x > 0:
        stack.push(x % base)
        x = x // base

    newNum = ""
    while not stack.is_empty():
        newNum += convertString[stack.pop()]

    return newNum

