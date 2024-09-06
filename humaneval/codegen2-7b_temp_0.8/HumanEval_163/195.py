
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    int_list = []
    for i in range(a, b+1):
        num_list = list(str(i))
        if num_list[0]%2 == 0:
            int_list.append(i)
    return int_list

