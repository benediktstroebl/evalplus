
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
    # 1. is a bigger than b?
    # 2. generate integers
    # 3. return even integers
    if a > b:
        a, b = b, a
    integers = [x for x in range(a, b+1)]
    even_integers = [x for x in integers if x % 2 == 0]
    return even_integers

