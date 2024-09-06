
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # A helper function to generate the digits in ascending order
    def generate_ascending(digits):
        digits.sort(key=lambda x: x // 2)
        return digits

    # The result list will be the concatenation of all the generated digits
    result = []

    # Generate digits from a to b
    for i in range(a, b + 1):
        digits = str(i)
        if len(digits) > 1:
            result.extend(generate_ascending(digits[1:]))

    return result
