
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    
    def only_evens(a):
        evens = []
        for i in str(a):
            if int(i) % 2 == 0:
                evens.append(int(i))
        return evens

    final_list = []
    if a % 2 == 0:
        final_list.extend(only_evens(a))
    elif a % 2!= 0:
        a += 1
        final_list.extend(only_evens(a))

    final_list.sort()

    return final_list

