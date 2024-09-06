```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    """
    if n <= 1:
        return [1]
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5/5, while n % i == 0):
        factors.append(i)
        n = n // i
    
    return factors

# Example usage
n = 25
print(factorize(n))  # Output: [5, 5]
```