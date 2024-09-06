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
    # Check if n is prime
    if n == 1:
        raise ValueError(f"{n} is not a prime number")
    else:
        while n > 1:
            # Keep track of the factors
            seen = set()
            # Find the last non-composite number
            i = len(seen) - 1
            while i >= 0 and seen[i] < n:
                i -= 1
            n_factors = len(seen) + 1
            while n > 1 and n_factors > 1:
                # Find the largest factor less than n
                l = len(factors_less_than_n)
                while l > 0 and factors_less_than_n[l - 1] > n:
                    l -= 1
                n_factors = n_factors * factors_less_than_n[l]
                # If the factor is not in the seen set, add it
                if n_factors not in seen:
                    seen.add(n_factors)
                    n -= n_factors
                    n_factors = 1
            # If there are any remaining factors, they are composite
            if n > 1:
                raise ValueError(f"{n} is not a prime number")
        # Return the list of prime factors in the order of smallest to largest
        return [i for i in seen if i > 1]

