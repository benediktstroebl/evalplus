
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # convert a and b to strings and convert each character to its ASCII value
    a_str = str(a)
    b_str = str(b)
    a_chars = [ord(c) for c in a_str]
    b_chars = [ord(c) for c in b_str]

    # initialize result list with the even digits
    result = [sum(a_chars[i:]) // 2 for i in range(len(b_chars))]

    # return the result list
    return result