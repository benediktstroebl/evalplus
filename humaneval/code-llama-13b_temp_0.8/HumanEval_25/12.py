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
    if n < 2:
        raise ValueError("Incorrect input value")

    result: List[int] = []

    # check for prime factors
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            # check for prime
            prime: bool = True
            for j in range(2, (i // 2) + 1):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                result.append(i)

    # check for non-prime factors
    for i in range(len(result)):
        k = result[i]
        while n % k == 0:
            n = n // k
        if n == 1:
            break

    if n > 1:
        result.append(n)

    return result

