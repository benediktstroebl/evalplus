
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return []

    # count the number of digits in the range [a, b]
    count = sum(map(str.isdigit, str(a)))
    count += sum(map(str.isdigit, str(b)))

    # return the even digits in the range
    return [int(x) for x in str(a) if str(a).isdigit(x) and str(a).isdigit(x - 1) % 2 == 0]
