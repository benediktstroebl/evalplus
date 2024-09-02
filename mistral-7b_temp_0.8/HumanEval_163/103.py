
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a < b:
        even_integers = []
        while a < b:
            if a % 2 == 0:
                even_integers.append(a)
            a += 1
        return even_integers
    elif a > b:
        even_integers = []
        while b < a:
            if b % 2 == 0:
                even_integers.append(b)
            b += 1
        return even_integers
    else:
        if a % 2 == 0:
            return [a]
        else:
            return []

