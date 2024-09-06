
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
    while a <= b:
        digit = a % 10
        a = a // 10
        if digit in result:
            # If the digit is already in the result, append the digit
            # in reverse order to the result
            result.append(digit)
            result.insert(0, -1)
        else:
            # If the digit is not already in the result, add it to
            # the result in ascending order
            result.append(digit)
        a = a // 10
    return result