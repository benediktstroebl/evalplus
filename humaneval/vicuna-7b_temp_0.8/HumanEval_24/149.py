

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return 1
    divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    while True:
        largest = 0
        for d in divisors:
            if n % d == 0 and d < n:
                largest = d
                break
        if largest == 0:
            return n
        divisors.remove(largest)
        for d in divisors:
            if d < largest * 2:
                break
        divisors.append(largest * 2)
    return largest
