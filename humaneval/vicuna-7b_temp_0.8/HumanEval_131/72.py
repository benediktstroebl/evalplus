
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Loop over digits, using an odd index variable i
    # Set the result variable r to the value of the digit at index i
    # Loop over all digits, using an odd index variable j
    # Set the result variable r to the value of the digit at index j
    r = 0
    for i in range(1, n+1):
        for j in range(i-1, n+1, 2):
            if (n % j) % 2 != 0:
                r *= j
    return r
