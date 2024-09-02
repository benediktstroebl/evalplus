from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # factorize an integer to a list of prime factors
    # using a while loop
    # 1. init with 2
    # 2. while num > 1:
    # 3.  while num % i == 0:
    # 4. num /= i
    # 5. return [i for i in nums]
    nums = []
    i = 2
    while n > 1:
        while n % i == 0:
            n /= i
            nums.append(i)
        i += 1
    return nums

