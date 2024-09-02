

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = 1
    for num in range(1, n + 1):
        if n % num == 0:
            if num > largest:
                largest = num
    return largest