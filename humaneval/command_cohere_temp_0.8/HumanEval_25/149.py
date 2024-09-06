```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.append(n)
    return factors
```

The code uses a simple algorithm factoring the number n by iterating over numbers from 2 to n and checking if the number is prime. If the number is prime, it is appended to the list of factors. Then, the code checks if the number can be further divided by the current prime and does so until the number is fully factored. Lastly, the last remaining number in the denominator (if any) is also added to the list of factors. The code is implemented using type hints and the `List` type is used to create a list of integers indicating prime factors.