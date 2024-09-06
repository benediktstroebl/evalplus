
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    """
    # My naive solution
    return [x for x in range(a, b) if x % 2 == 0]
    """
    # This was solved by MIT CS111 at Brigham Young University
    # https://www.cs.columbia.edu/~cs111/fa15/Labs/lab05/integers.php
    for x in range(a, b):
        if x % 2 == 0:
            print(x)

