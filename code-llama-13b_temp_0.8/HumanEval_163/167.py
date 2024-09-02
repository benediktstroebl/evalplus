
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # return []
    result = []
    for number in range(a, b + 1):
        str_num = str(number)
        if str_num[-1] == '0':
            continue
        for char in str_num:
            if int(char) % 2 == 0:
                result.append(int(char))
    return sorted(result)

