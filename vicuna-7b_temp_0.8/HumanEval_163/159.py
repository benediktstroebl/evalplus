
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # check for bounds
    if a > b:
        return []
    # check if the range of the first number is 2
    if (a % 2 == 0 and a >= 2) or (b % 2 == 0 and b >= 2):
        # check if the last number in the range is a multiple of 2
        last_digit = a if a > b else b
        # if the last number is even, return the digits in ascending order
        if last_digit % 2 == 0:
            return [last_digit]
        # if the last number is odd, return the digits in descending order
        else:
            last_two = last_digit // 2
            return [last_two, last_digit % 2] + generate_integers(a, b - last_two)
    # if the first number is odd, return the digits in descending order
    else:
        return [a] + generate_integers(b, 0)
