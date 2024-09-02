
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def _is_even_digit(n):
        return n % 2 == 0
    return list(filter(_is_even_digit, range(min(a, b), max(a, b) + 1)))
    
