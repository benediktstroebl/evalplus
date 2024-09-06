
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return []
    if b - a == 1:
        return [a]
    even_digits = []
    for i in range(a, b):
        if i % 2 == 0:
            even_digits.append(i)
    return sorted(even_dig
