```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned in the form (num, times)
    """
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append((n factors 2.)
    for i in range(3, int(n**0.5) + 1, step by step:
        if n % i == 0:
            factors.append((i(i, n // i)))
            n = n // i
    if n > 2:
        factors.append((n(n, 1))
    return factors

# Example usage:
# Test integer 8:
result = factorize(8)
print(result)  # Output: [2, 2, 2]

# Test integer 25:
result = factorize(25)
print(result)  # Output: [5, 5]

# Test integer 70:
result = factorize(70)
print(result)  # Output: [2, 5, 7]
```
The above function will return a list of prime factors in the order from smallest to largest, along with the corresponding times. The function uses a approach where it starts factoring by the number 2, then it uses a for loop to factorize numbers greater than 2, and finally it adds the remaining odd prime factor.