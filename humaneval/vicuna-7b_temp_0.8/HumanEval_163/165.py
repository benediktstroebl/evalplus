
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b < a:
        return []

    result = []
    while b > a:
        # Find the smallest odd number greater than a
        for odd in range(a+1, b+1, 2):
            if odd % 2 == 1:
                break
        else:
            b -= 2
        result.append(odd)

    # The remaining digits are the even digits between a and b
    for i in range(a, b):
        result.append(i)

    return result