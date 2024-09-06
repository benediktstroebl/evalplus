
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    for i in range(a, b+1):
        if str(i) != str(i)[::-1]:
            continue
        even = True
        for j in str(i):
            if int(j) % 2 != 0:
                even = False
                break
        if even:
            result.append(i)
    return result

