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
    # Function uses trial and error approach, not using any specific algorithm
    # As a result, it might not be the most efficient way to solve the problem
    # However, it is a simple and easy to understand
    # Also, it is suitable for small and medium-size inputs
    # If the input is too big, it may take a long time to run
    # To optimize the function, we could use more sophisticated algorithms
    # Such as the trial division or Miller-Rabin primality test
    # However, the current implementation should be sufficient for educational purposes
    
    # Check if input number is prime
    if n > 1:
        # If not, return an empty list
        return []
    
    # If input number is prime, list of factors
    factors = [n]
    while n > 2:
        # Get the number of factors of n
        n_factors = factorization(n)
        
        # Update the list of factors
        factors = factors + n_factors
        
        # Get the next number to check
        next_n = n // 2
        
        # If n is even, check it again
        if next_n > 2:
            # If next_n is prime, add its factors to the list
            if is_prime(next_n):
                factors = factors + next_n_factors(next_n)
            else:
                # Otherwise, add the factors of n and n/2
                factors = factors + n_factors(n) + n_factors(next_n)
        
        # Decrement the number to check
        n = next_n
    
    # If the input is not prime, return an empty list
    return []

