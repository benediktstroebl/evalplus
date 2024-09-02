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
    if n in (0, 1, 2):
        return
    if n == 2:
        return [2]
    max_prime = int(n ** 0.5)
    prime_list = [2]
    for i in range(3, max_prime + 1):
        if n % i == 0:
            prime_list.append(i)
            while n % i == 0:
                n //= i
    if n != 1:
        prime_list.append(n)
    return prime_list

