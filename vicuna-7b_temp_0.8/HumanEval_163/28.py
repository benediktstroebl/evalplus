
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # If a is less than b, we can return the digits in either order
    # If a is equal to b, we can return the digits in ascending order
    # Otherwise, we can return the digits in descending order
    if a <= b:
        return [int(i) for i in str(a) if i.is_integer() and i >= 0]
    else:
        return [int(i) for i in str(b) if i.is_integer() and i >= 0]
