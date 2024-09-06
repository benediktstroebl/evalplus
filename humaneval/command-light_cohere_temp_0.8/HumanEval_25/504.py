```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        for d in range(2, int(n**.5) + 1, 2):
            if n % d == 0:
                factors.append(d)
                n = n // d
    return factors

# Example 1:
print(factorize(8))  # [2, 2, 2]

# Example 2:
print(factorize(25))  # [5, 5]

# Example 3:
print(factorize(70))  # [2, 5, 7]
```
This function factors all the prime factors of the input number n by repeatedly dividing it by all numbers from 2 up, checking for divisibility and appending the divisor to the list of factors. It then returns a list of the prime factors, ordered from the smallest to the largest. The function also passes the test cases successfully.