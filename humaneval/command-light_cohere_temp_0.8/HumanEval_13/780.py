Here is a Python script with a self-contained function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
import math
def greatest_common_divisor(a, b):
    if math.gcd(a, b) == 1:
        return a
    elif math.gcd(a, b) == math.gcd(b, a):
        return b
    else:
        # Find the prime factorization of a and b
        pa = power(prime_factors(a), int(math.gcd(a, b)))
        pb = power(prime_factors(b), int(math.gcd(a, b)))
        return max(pa, pb)

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
```
This script defines a function `greatest_common_divisor` that computes the GCD of two numbers and finds their respective prime factors. 
The function uses the `prime_factors` to find the prime factors of the given number n, which are stored in a list. The function then calculates the product of the prime factors of the given GCD and returns the maximum of those products.