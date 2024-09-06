

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_divisor = 1
    for i in range(1, n + 1):
        if n % i == 0 and i < n / i:
            max_divisor = i
            break
    return max_divisor

print(largest_divisor(60))
