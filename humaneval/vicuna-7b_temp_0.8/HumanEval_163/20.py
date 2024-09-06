
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
        if str(num) == str(num//2):
            result.append(num)
            while num > 0:
                if str(num) == str(num//2):
                    result.append(num)
                num = num // 2
    return result