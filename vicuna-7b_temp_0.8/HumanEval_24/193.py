

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Loop through the numbers 2 to n-1
    for i in range(2, n-1):
        # If n divides i, it cannot be the largest
        if n % i == 0:
            break
        # If n does not divide i, i must be the largest
        else:
            return i
    # If we reach the end of the loop, the largest divisor is the smallest number that divides n evenly
    return n
