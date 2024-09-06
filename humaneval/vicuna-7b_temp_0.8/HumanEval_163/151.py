
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Handle the base cases where a is less than b.
    if a < b:
        return []

    # Handle the case where b is even.
    if b % 2 == 0:
        # If a is less than b/2, return all digits of b.
        if a < b // 2:
            return [str(b)[:a]]
        # If a is greater than or equal to b/2, return all digits of b
        # and append a to the list.
        else:
            return [str(b)[:a], a]

    # Handle the case where b is odd.
    else:
        # If a is less than b/2, return all digits of b.
        if a < b // 2:
            return [str(b)[:a]]
        # If a is greater than or equal to b/2, return all digits of b
        # and append a to the list.
        else:
            return [str(b)[:a], a]
