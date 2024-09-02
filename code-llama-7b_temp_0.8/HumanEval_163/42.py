
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    numbers = []
    for i in range(a, b + 1):
        number = str(i)
        if '1' in number or '3' in number or '5' in number or '7' in number or '9' in number:
            continue
        if '0' in number:
            number = number[1:]
        numbers.append(int(number))
    return numbers

