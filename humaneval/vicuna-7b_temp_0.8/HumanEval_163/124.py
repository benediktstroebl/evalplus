
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Find the first number in the range that is evenly divisible by n.
    while a % n for a in range(b+1, int(n*b)//n):
        n = n//2
    # Initialize a list with the even digits in ascending order.
    digits = []
    # Append the even digits of the current number to the list.
    for i in range(a, b+1):
        digits.append(i%2)
    return digits
