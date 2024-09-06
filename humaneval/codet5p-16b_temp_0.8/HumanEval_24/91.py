

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    
    largest = 1
    for num in range(2, n):
        if n % num == 0:
            largest = num
    return largest
