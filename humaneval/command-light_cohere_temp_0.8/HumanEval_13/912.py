```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input must be numbers")

    # Calculate the prime factorization of both numbers
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)

    # Find the greatest common divisor of the prime factors
    gcd_prime = max(factors_a[-1], factors_b[-1])

    # Apply the gcd algorithm to find the greatest common divisor
    return gcd(tuple(factors_a), tuple(factors_b))

def prime_factors(n: int) -> list:
    primes = []
    while n > 1:
        if n % 2 == 0:
            primes.append(2)
        n //= 2
        while n % 3 == 0:
            primes.append(3)
            n //= 3
    primes.append(n)
    return primes

def gcd(a: tuple, b: tuple) -> int:
    if len(a) != len(b):
        raise ValueError("Arguments must be of equal length")
    return sum(p1 * p2 for p1, p2 in zip(a, b))

try:
    print(greatest_common_divisor(3, 5))
    print(greatest_common_divisor(25, 15))
    print(greatest_common_divisor(10, 15))
except ValueError as e:
    print("Error:", str(e))
```