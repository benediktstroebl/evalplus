
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even = []
    a = int(a)
    b = int(b)
    for i in range(a, b + 1):
        if i >= 10:
            x = str(i)
            if x[0] == '2' or x[0] == '4' or x[0] == '6' or x[0] == '8':
                even.append(i)
        if i >= 2:
            x = str(i)
            if x[1] == '2' or x[1] == '4' or x[1] == '6' or x[1] == '8':
                even.append(i)
        if i >= 4:
            x = str(i)
            if x[2] == '2' or x[2] == '4' or x[2] == '6' or x[2] == '8':
                even.append(i)
        if i >= 6:
            x = str(i)
            if x[3] == '2' or x[3] == '4' or x[3] == '6' or x[3] == '8':
                even.append(i)
    return even
