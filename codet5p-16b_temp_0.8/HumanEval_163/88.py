
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    
    # m = min(a, b)
    # n = max(a, b)
    # even_list = []
    # if m % 2 == 0:
    #     even_list.append(m)
    # for i in range(m+1, n+1, 2):
    #     even_list.append(i)

    even_list = [i for i in range(a, b+1) if i % 2 == 0]
    return even_list


