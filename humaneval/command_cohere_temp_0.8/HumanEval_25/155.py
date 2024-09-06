```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != n // i:
            factors.append(i)
            while is_factor:
                n //= i
                is_factor = n % i == 0
                if is_factor:
                    factors.append(i)
    return factors
```
The problem asks to create a function that takes an integer as an argument and returns a list of its prime factors. Each factor is listed in the list only once, and the factors are ordered from smallest to largest. To solve this, the function `factorize` is created, which iterates through all integers from 2 up to `n` and checks if they are a factor using the modulo operator. When a factor is found, it is appended to the list `factors`, and then the code checks if any other factor can be derived from the current factor, doing this iteratively until all factors are found. As expected, this approach can efficiently solve the problem because it doesn't need to check all possible combinations like a brute force approach would do. It also doesn't make any unnecessary expensive prime-number-checking calculations, which makes it efficient as well.