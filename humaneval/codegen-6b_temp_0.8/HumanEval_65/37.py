
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # First figure out how many digits we have to start with
    n = 1
    while (2 ** n) <= x:
        n += 1
    if n == 1:
        return str(x)

    # Next figure out how many digits we have to end with
    n -= 1
    while (2 ** n) < x:
        n -= 1
    if n == 0:
        return str(x)

    # Now we know that we will start with n digits and we will end with n-1
    # digits converted to string

    # Figure out how many digits to remove
    num_to_remove = (2 ** n) - n - 1

    # Remove that many digits from the initial number
    x -= (2 ** n) - 1
    x //= 10 ** (n - 1)

    # Convert the remaining digits to string
    x = str(x)

    # Now remove those digits
    for i in range(num_to_remove):
        x = x[1:] + x[:1]

    # Return the result as a string
    return x
