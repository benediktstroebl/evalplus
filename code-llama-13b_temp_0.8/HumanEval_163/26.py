
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def is_even(num):
        return num % 2 == 0

    result = []
    for i in range(a, b + 1):
        # Use a list comprehension to convert the digits to integers
        if all(is_even(int(c)) for c in str(i)):
            result.append(i)
    return result

