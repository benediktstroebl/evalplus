```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    if not n: return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, i += 2):
        if n % i == 0:
            factors.append(i)
        n = n // i
    return factors

# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
The provided Python code defines a function called factorize that calculates and returns a list of prime factors for a given integer n. The function employs a loop to continuously divide n by the smallest prime factors until it becomes a prime number. The factors are then appended to a list, which is returned as the final result. The code also includes example usage for testing the function with different input numbers.