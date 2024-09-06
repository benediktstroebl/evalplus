
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Find the first digit that is greater than b and return it.
    while b > 0:
        b, d = divmod(b, 10)
        if d > b:
            break
    d = d // 10
    # If there is no digit greater than b, return [].
    if d == 0:
        return []
    # Get all the even digits in the range a..b.
    digits = [str(d)]
    d += 1
    while d < b:
        d, d = divmod(d, 10)
        digits.append(str(d))
    return digits
