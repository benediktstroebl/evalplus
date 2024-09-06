```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.extend([count] * count)
    if n > 1:
        factors.append(n)
        factors.extend([1] * (n - 1))
    return factors
```

The code employs an iterative method to find the prime factors of `n`, repeatedly dividing `n` by the current factor when it is found. To accommodate multiple occurrences of the same factor in the prime factorization, the code uses the `count` variable to track the number of times the factor appears in the factorization and appends it to the `factors` list. This ensures that the prime factors are listed in descending order and accompanied by their corresponding counts.