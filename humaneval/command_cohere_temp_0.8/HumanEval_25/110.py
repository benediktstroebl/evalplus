```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for divisor in range(2, n):
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                n //= divisor
                count += 1
            if count > 0:
                factors.append(divisor)
                factors.extend([divisor] * count)
    if n > 1: 
        factors.append(n)
    return factors
```
The factorization algorithm loops through all divisors from 2 to the given number `n`. 

When a divisor is found, the algorithm enters the inner loop and divides `n` by this divisor as many times as possible until it isn't divisible anymore. The number of iterations of this inner loop is stored in the `count` variable and used to determine the number of times the divisor should be appended to the list of factors. Factors are extended using a list comprehension, which is a more efficient way to repeat elements multiple times.

After the while loop, the `n` variable will have the last divisor remaining, and if it's greater than 1, it will be appended to the list of factors. This ensures that the input number is always factored fully, and the list of factors contains all prime factors and their corresponding counts.