
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Your code here.
    result = []
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        s = str(i)
        for digit in s:
            if int(digit) % 2 == 0:
                result.append(int(digit))
    return result
