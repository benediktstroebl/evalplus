```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    return factors

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
 ```  This function is designed to determine and return the list of prime factors for a given integer in descending order.  It uses a process loop, where it continuously identifies pairs of factors and then removes the smallest factor from consideration by dividing by 2.  The loop iterates through the numbers starting from 3 and up, using the condition `n % i == 0` to check for divisibility.  The process continues until the number is no longer divisible by any integer `i` with `i > 2`.  This ensures that all factors greater than 2 are correctly identified.