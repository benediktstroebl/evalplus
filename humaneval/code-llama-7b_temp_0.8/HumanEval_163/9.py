
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a_list = list(str(a))
    b_list = list(str(b))
    if a > b:
        a_list, b_list = b_list, a_list
    result_list = []
    for i in range(0, len(b_list)):
        for j in range(0, len(a_list)):
            if a_list[j] > b_list[i]:
                break
            if b_list[i] == a_list[j]:
                continue
            if b_list[i] >= a_list[j]:
                if a_list[j] % 2 == 0:
                    result_list.append(int(a_list[j]))
    return sorted(result_list)

