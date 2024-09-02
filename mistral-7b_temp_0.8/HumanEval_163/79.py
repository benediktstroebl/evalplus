
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # 1
    # Generate numbers between a and b
    nums = list(range(a, b + 1))

    # 2
    # Filter out even numbers
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)

    # 3
    # Sort the result
    result.sort()

    return result
