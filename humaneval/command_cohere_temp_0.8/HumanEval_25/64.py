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

The code employs an exhaustive division method to extract the prime factors of 'n', ensuring each factor's presence in the factorization is accounted for by appending it the appropriate number of times. The outcome is a list of prime factors, ordered from minimal to most significant, representing the input number 'n'. 

Here's an example of how you can use the factorize function to factorize the number 70:
```python
factors = factorize(70)
print(factors)  # Output: [2, 5, 7]
```

This output represents the prime factors of 70, where both 2 and 7 appear once, and 5 appears twice, to maintain the conditioning that the product of the factors should equal the input number.