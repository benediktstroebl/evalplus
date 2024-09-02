
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a <= 0 or b <= 0:
        raise ValueError("The parameters must be positive integers.")
    if a > b:
        raise ValueError("The maximum of the parameters must be greater than the minimum.")
    if a % 2!= 0 or b % 2!= 0:
        raise ValueError("The parameters must be an even number.")

    return [a, b]
