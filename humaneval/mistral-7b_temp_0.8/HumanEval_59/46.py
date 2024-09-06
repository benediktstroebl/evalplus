

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # TODO: fill in the solution here!
    # 这题的关键在于如何知道分解出来的整数如何组合得到n
    # 而这个关键要从一个数1开始，逐步求得这个数的最大素因子
    # 直到不能再分解，那么这个分解的数就是最大的素因子了
    # 下面是解法：
    # 首先声明一个数为素因子
    prime_factor = 2
    # 声明一个数为全部的因子
    all_factors = 2
    # 声明一个变量保存最大的因子
    max_factor = 2
    # 当整数大于1且不为素数时循环
    while n > 1 and n%all_factors != 0:
        # 这里如何判断素数？
        # 如果能被自己整除的话，则不是素数
        # 如果能被
