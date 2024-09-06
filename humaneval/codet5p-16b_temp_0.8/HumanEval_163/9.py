
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    if a % 2 == 1 or b % 2 == 1:
        return []
    else:
        start = a
        end = b
        even_digits = []
        while start <= end:
            if start % 2 == 0:
                even_digits.append(start)
            start += 1
        return even_digits
