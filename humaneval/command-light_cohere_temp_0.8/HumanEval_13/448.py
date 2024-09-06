```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")
    if a == 0:
        return 0

    # Compute the prime factorization of a and b
    prime_fa = []
    for i in range(2, min(len(math.fs(a) // 2) + 1):
        while a % i == 0:
            prime_fa.append(i)
            a = a // i
        a = a // i

    prime_fb = []
    for i in range(2, min(len(math.fs(b) // 2) + 1):
        while b % i == 0:
            prime_fb.append(i)
            b = b // i
        b = b // i

    # Find the highest common divisor of the prime factorizations
    common_divisor = max(prime_fa, prime_fb)

    return common_divisor
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. It first checks if either input is non-existent or zero and raises a `ValueError`. Then, it computes the prime factorization of both numbers and identifies the highest shared prime factor as the greatest common divisor.