```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != 1:
            factors.append(i)
            n //= i
        if n == 1:
            break
    return factors
```
This Python script defines a function called factorize(n: int) -> List[int]: that takes in an integer n as input and returns a list of its prime factors. It starts by creating an empty list called factors to store the prime factors. It then iterates through numbers from 2 up to n itself, checking for divisibility by testing if n is divisible by i with no remainder (n % i == 0). If i is a factor and not equal to 1, it adds i to the factors list and divides n by i to continue searching for other factors. Once n becomes 1, it stops iterating as all prime factors have been found. Finally, it returns the factors list containing all the prime factors of n in ascending order, each repeated accordingly based on its multiplicity in the factorization.