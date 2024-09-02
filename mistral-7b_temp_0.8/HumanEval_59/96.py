

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # 只要小于 n 的数组都有一个大于 n 的倍数，则 n 不可能是最大的质数
    if n < 2:
        return 1
    # 因为只有奇数是质数，所以从 3 开始查找
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n //= i
    return n

