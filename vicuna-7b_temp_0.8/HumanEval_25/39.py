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
    # Check if the input number is prime
    if n < 2:
        raise ValueError("Input number is not prime")
    if n == 2:
        return [n]
    prime_factors = [n]
    while n != 1:
        # Find the last prime factor
        last_prime_index = len(prime_factors) - 1
        last_prime_value = prime_factors[-1]
        for index in range(last_prime_index, len(prime_factors)):
            if prime_factors[index] % last_prime_value == 0:
                last_prime_index = index
                last_prime_value = prime_factors[index]
        # Remove last prime factor and all smaller factors
        prime_factors.pop(last_prime_index)
        for i in range(last_prime_index, len(prime_factors)):
            prime_factors[i] = prime_factors[i] // last_prime_value
    return prime_factors