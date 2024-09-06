```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5 / 2) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
def test_factorize():
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
``` 
The function factorize returns a list of prime factors of the given number in the order from smallest to largest. 
The test_factorize function tests the function with three different numbers, and prints the list of prime factors for each number.