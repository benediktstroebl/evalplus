
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def is_even(n):
        return (n % 2) == 0

    def next_even(n):
        """
        Given a positive integer n, returns the next even number.
        """
        return n + (n % 2)

    # Get the next even number greater than or equal to a.
    a = next_even(a)

    # Keep increasing the even number, until it's greater than b.
    ans = []
    while a <= b:
        ans.append(a)
        a = next_even(a)

    return ans

