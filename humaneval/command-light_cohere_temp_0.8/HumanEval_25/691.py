```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    """
   
    smallest prime factors of n
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i

    for j in range(int(n**0.5) + 1, while n % j == 0:
        factors.append(j)
        n = n // j

    return factors

# Example usage:
n = int(input("Enter a number: "))
factors = factorize(n)
print(f"Prime factors of {n}: {factors}")
```
This code defines a function factorize that returns a list of prime factors of the given integer n, ordered from the smallest to largest. It uses a approach to find the prime factors, by iterating through the divisibility table up to the square root of n, checking for divisibility and appending the prime factor to the factors list.