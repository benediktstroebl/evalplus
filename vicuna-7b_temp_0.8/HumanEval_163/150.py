
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Handle the base case where a and b have different parity.
    if a % 2 != b % 2:
        # We can't generate any even digits in this case.
        return []
    # For the other cases, we can use binary search.
    if a == 1:
        # We can generate the even digits from 2 to b-1.
        return [2, 4, 6, 8]
    else:
        # We can generate the even digits from 2 to a-1, and then
        # continue generating from the beginning of the list up to b-1.
        return [2, 4, 6, 8, a//2] + generate_integers(a//2+1, b-1)
