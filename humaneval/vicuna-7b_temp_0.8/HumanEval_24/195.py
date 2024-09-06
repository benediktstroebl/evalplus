

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    while len(divisors) < n:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i % j == 0:
                    divisors.append(j)
                    if j > i:
                        break
    return divisors[-1]
