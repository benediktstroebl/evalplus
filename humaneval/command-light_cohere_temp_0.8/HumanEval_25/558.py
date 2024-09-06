```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int(n))
    return factors

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
 ```
This function recursively factors an input number n into a list of its prime factors, it starts by adding 2 to the list until the number is not divisible by 2, then it iterates through the numbers from 3 up, checking for divisibility, and adding each prime factor to the list. The function then calculates the prime factors of the input number n in the order from smallest to largest.