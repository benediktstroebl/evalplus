
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Base cases
    if n < 0:
        raise ValueError('must be a positive integer')
    if n == 0:
        return 0

    # Initialize
    prod = 1
    m = n

    # Initialize set of even digits
    evens = set(str(x) for x in range(10) if x % 2 == 0)

    # Iterate until we reach base case (single digit)
    while len(str(m)) > 1:
        # Extract last digit
        d = m % 10
        # Update product of digits
        if str(d) not in evens:
            prod *= d
        m //= 10

    return prod

