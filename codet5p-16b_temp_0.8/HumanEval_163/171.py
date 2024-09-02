
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    a = str(a)
    b = str(b)
    answer = []
    for x in range(int(a[0]), int(b[0])+1):
        if x % 2 == 0:
            answer.append(x)
    return answer
