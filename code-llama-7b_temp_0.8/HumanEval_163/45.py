
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a_string = str(a)
    b_string = str(b)
    a_list = [int(x) for x in a_string if x in '2468']
    b_list = [int(x) for x in b_string if x in '2468']
    common_list = sorted(list(set(a_list) & set(b_list)))
    return common_list
