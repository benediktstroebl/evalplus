

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        raise ValueError('Can not find divisor of non-positive number')
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    else:
        for i in range(1, n):
            if n % i == 0:
                dp[n] = i
                return dp[n]
        dp[n] = n
        return dp[n]
