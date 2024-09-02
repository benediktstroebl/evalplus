
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a == b:
        return []

    min_ = min(a, b)
    max_ = max(a, b)

    result = []

    for number in range(min_, max_ + 1):
        number_string = str(number)

        for digit in number_string:
            if digit not in result and int(digit) % 2 == 0:
                result.append(digit)

    return result

