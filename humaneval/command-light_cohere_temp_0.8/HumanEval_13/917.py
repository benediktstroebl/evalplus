```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer.")
    elif a == 0 or b == 0:
        return 0

    # Calculate the prime factorization of a and b
    a_prime_factors = prime_factors(a)
    b_prime_factors = prime_factors(b)

    # Find the greatest common prime factor
    common_prime = max(a_prime_factors, b_prime_factors)

    # Return the product of all common prime factors and 1
    result = 1
    for p in common_prime:
        result *= p

    return result

def prime_factors(n: int) -> List[int]:
    """ Return the prime factors of the given number """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5)):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
``` 
This script defines a function that computes the greatest common divisor of two numbers by finding their prime factors and identifying the greatest common prime factor.