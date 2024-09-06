
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    even_numbers = []
    for n in range(a, b + 1):
        str_n = str(n)
        for d in str_n:
            if int(d) % 2 != 0:
                break
        else:
            even_numbers.append(n)

    return even_numbers
