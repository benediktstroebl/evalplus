
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
        a, b = b, a

    # Brute-force solution
    result = []
    for i in range(a, b):
        for digit in str(i):
            if int(digit) % 2 == 1:
                break
        else:
            result.append(i)

    return result

