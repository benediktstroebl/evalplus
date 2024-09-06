
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # TODO: write your code here
    if a > b:
        a, b = b, a
    result = []
    for i in range(a, b + 1):
        num_str = str(i)
        if len(num_str) % 2 == 0 and num_str[0] != '-' and num_str[0] != '0':
            result.append(int(num_str[::2]))
    return result
