
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Your code here
    a_digits = [d for d in str(a)]
    b_digits = [d for d in str(b)]

    a_digits.sort(key=lambda x: int(x))
    b_digits.sort(key=lambda x: int(x))
    if a_digits[-1] > b_digits[-1]:
        return []
    else:
        return list(range(a, b, 2))
