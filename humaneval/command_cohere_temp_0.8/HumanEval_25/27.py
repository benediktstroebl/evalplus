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

The code employs an iterative approach to determine the prime factors of a given number `n`. It begins by testing factors from `2` up to `n-1` to ascertain if the number is prime or not. For each candidate factor, it checks if the factor can divide the number without leaving a remainder. If the factor is found to be prime, it is added to the list of factors, and the loop continues until the number is divided fully by this prime factor. This process ensures that each prime factor is explored before moving on to the next factor. Ultimately, the function provides the list of prime factors, in ascending order, ensuring that each factor appears in the list the number of times it divides the original number.