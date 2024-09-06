

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [2]
    largest = 1
    for num in divisors:
        if n % num == 0:
            if n // num > largest:
                largest = n // num
    return largest
