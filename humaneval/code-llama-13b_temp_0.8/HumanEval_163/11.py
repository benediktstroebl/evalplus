
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    results = []
    for i in range(a, b + 1):
        s = str(i)
        for c in s:
            if c.isdigit() and int(c) % 2 != 0:
                break
        else:
            results.append(i)

    return results
