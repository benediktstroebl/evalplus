

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # n >= 1
    if n == 1:
        return 1
    # n > 1
    largest = 0
    for i in range(1, n):
        # check if i divides n evenly
        if n % i == 0:
            # check if i is larger than largest number we have seen so far
            if i > largest:
                largest = i
    return largest
