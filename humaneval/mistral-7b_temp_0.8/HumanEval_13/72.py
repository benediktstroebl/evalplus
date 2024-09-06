

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # returns (a//b, a%b) if b != 0 else (a, 0)
    def _divide(a: int, b: int) -> (int, int):
        if b == 0:
            return (a, 0)
        return (a // b, a % b)
    # if a == b return a
    if a == b:
        return a
    # if a < b, swap a, b
    if a < b:
        a, b = b, a
    # while b != 0
    while b != 0:
        # get next a, b pair
        (a, b) = _divide(a, b)
    return a

