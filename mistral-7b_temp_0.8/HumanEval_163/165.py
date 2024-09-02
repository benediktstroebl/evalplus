
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Your code here
    a = int(a)
    b = int(b)
    even = []
    if a > b:
        for x in range(a, b):
            if x % 2 == 0:
                even.append(x)
        return even
    if b > a:
        for x in range(a, b):
            if x % 2 == 0:
                even.append(x)
        return even
