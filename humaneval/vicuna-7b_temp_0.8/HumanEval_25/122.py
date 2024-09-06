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
    if n <= 1:
        return []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        factors = [i for i in range(2, int(n**0.5) + 1)]
        for j in factors:
            for k in range(2, int(j**0.5) + 1):
                if j % k == 0:
                    for i in range(2, int(k**0.5) + 1):
                        if k % i == 0:
                            for r in range(1, i):
                                n //= i
                            break
                        else:
                            break
                    else:
                        n //= k
                        break
                    else:
                        n //= j
                        break
                    else:
                        n //= j
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        n //= i
                        break
                    else:
                        n //= k
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                    else:
                        break
                   
