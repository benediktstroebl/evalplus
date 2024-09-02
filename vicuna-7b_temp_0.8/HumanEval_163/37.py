
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # if a is greater than b, it means that there is no even digit between a and b
    # so we can return an empty list here
    if a > b:
        return []

    # otherwise, we know that the first digit must be an even digit between a and b
    # so we can find the first even digit and then start adding the remaining digits
    # in ascending order
    first_even_digit = a % 2 == 0
    first_digit = a // 2 if first_even_digit else 0
    result = [first_digit]
    for i in range(1, b - a + 1):
        # we can use division here instead of modulo, because we already know that
        # the first digit is an even digit between a and b
        next_digit = (a // 2) + i
        if next_digit >= b:
            break
        result.append(next_digit)

    return result
