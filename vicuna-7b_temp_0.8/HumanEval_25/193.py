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
    # check if n is prime
    if n == 1:
        return [1]
    elif n == 2:
        return [2]
    else:
        # find all factors
        factors = []
        while n > 1:
            if n % 2 != 0:
                factors.append(2)
            if n % 3 != 0:
                factors.append(3)
            n = n / 6
        # sort factors
        factors.sort()
        # put each factor in the right place
        i = 0
        while i < len(factors):
            if factors[i] == 2:
                factors[i] = 2, 1
            elif factors[i] == 3:
                factors[i] = 3, 1
            elif factors[i] > n:
                break
            else:
                i += 1
        # put the remaining factors in the correct place
        j = i + 1
        while j < len(factors):
            if factors[j] > n:
                factors.insert(i + 1, factors[j])
                break
            else:
                j += 1
        return factors
