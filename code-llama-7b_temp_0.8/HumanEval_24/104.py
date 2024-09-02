

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Keep track of the largest number that divides n evenly.
    largest = 1

    # Loop through every number from 2 up to but not including n, incrementing by 1.
    for i in range(2, n):
        # If the current number is a factor of n, set largest to that number.
        if n % i == 0:
            largest = i

    # Return the largest number that divides n evenly.
    return largest
