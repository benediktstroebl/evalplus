
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    a = int(a)
    b = int(b)
    new_list = []
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        i = str(i)
        if i[-1] == '0' and i[-2] == '0':
            continue
        if i[-1] == '0' and i[-2] == '2':
            continue
        if i[-1] == '2' and i[-2] == '0':
            continue
        if i[-1] == '2' and i[-2] == '2':
            continue
        new_list.append(int(i[-2:]))
    new_list = sorted(new_list)
    return new_list
