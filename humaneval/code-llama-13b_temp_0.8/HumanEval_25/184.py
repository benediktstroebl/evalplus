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
    if n <= 0:
        raise ValueError('Input should be positive integer')
    elif n < 2:
        return []
    prime = [2, 3, 5]
    if n in prime:
        return [n]
    for i in range(len(prime)):
        if n % prime[i] == 0:
            return [prime[i]] + factorize(int(n / prime[i]))
    for i in range(6, int(n), 2):
        if i not in prime:
            for j in range(2, int(i)):
                if i % j == 0:
                    break
            else:
                prime.append(i)
                if n % i == 0:
                    return [i] + factorize(int(n / i))
    return []

