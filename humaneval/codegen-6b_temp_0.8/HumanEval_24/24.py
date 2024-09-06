

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    not_prime = [False] * (n + 1)
    for i in range(2, n):
        if not not_prime[i]:
            j = i * 2
            while j <= n:
                not_prime[j] = True
                j += i
    divisors = [i for i in range(2, n) if not_prime[i]]
    return max(divisors)

