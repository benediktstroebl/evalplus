
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
    for num in range(a, b+1):
        num = str(num)
        if num[0] in '01' and num[1] in '01':
            num = '0' + num
        if num in '2468':
            result.append(num)
    return result
