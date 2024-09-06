

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # 写出主要思路
    # 1. 因子分解
    # 2. 记录最大的质数因子
    # 3. 如果分解的因子是质数，那么最大的质数因子就是该因子
    # 4. 如果分解的因子不是质数，那么最大的质数因子就是最大的质数因子
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            n //= i
    return n

