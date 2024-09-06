
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # use sieve of eratosthenes to filter out non-even numbers
    if a > b:
        return []
    n = a + b
    # initialize list to store even numbers
    evens = []
    # iterate over all numbers from a to n
    for i in range(a, n + 1):
        # if the number is even, append it to evens
        if i % 2 == 0:
            evens.append(i)
    return evens
