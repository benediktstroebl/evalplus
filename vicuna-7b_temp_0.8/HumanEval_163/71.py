
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Convert a and b to 32-bit integers
    a = py32.to32(a)
    b = py32.to32(b)

    # Create a list to store the even digits
    digits = []

    # Loop through the range from a to b
    for i in range(a, b+1):
        # Get the digits of the current number
        digits.append(py32.int32(i))

    # Extract the even digits from the list
    return py32.int32(sum(d % 2 == 0 for d in digits))
