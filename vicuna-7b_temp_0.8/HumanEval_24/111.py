

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [2]
    for i in range(2, n + 1):
        for j in divisors:
            if (j % i == 0):
                divisors.append(j)
                break
        if j == n:
            return j
    return n
