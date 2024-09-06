
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
    int_list = []
    for i in range(a, b + 1):
        int_str = str(i)
        if int_str[0] in ['2', '4', '6', '8']:
            int_list.append(i)
    return int_list
