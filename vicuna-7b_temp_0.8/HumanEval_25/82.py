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
    factors = {}
    for i in range(1, n+1):
        for j in range(i**2, n+1, i):
            key = (i, j)
            if key not in factors:
                factors[key] = 1
            else:
                factors[key] += 1

    result = []
    for key in factors.items():
        result.append(key[0])
        for factor in factors[key]:
            result.append(factor*factor)

    return result


n = List(int).from_string("1 2 3 4 5 6 7 8 9 10 11 12")
result = factorize(n[0])
for i in range(1, len(n)):
    n[i] = n[i-1]*result[0]
result = [int(i) for i in n]
