
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    integers = []
    for i in range(a, b+1):
        for j in range(1, 10):
            if i//10 == j or i%10 == j:
                if j % 2 == 0:
                    integers.append(j)
    return integers
