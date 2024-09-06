

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return 1
    largest = 1
    smallest = n
    while n > largest:
        if n % largest == 0:
            smallest = n // largest
        else:
            if n % (smallest + 1) == 0:
                return smallest + 1
            else:
                largest += 1
    return 1

