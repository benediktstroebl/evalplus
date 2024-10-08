
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
        a, b = b, a
    output = []
    for i in range(a, b + 1):
        if str(i).isdigit() and int(i) % 2 == 0:
            output.append(i)
    return output
