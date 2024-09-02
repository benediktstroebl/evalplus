
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        raise ValueError("Can't handle negative numbers.")

    digits = str(num)
    if digits[0] == '0':
        digits = digits[1:]
    n = len(digits)
    return n // 2, (n // 2) % 2
