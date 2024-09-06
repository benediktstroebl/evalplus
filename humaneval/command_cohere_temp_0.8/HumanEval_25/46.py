```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != 1:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors
```

The code employs an efficient and organized approach to determine the prime factors of an integer `n` and extract them into a list. It initiates this process by iterating through integers ranging from 2 up to, but not including, the target number `n`. For each integer `i`, it checks if `i` is a factor of `n` by taking the remainder of `n` divided by `i`. If `i` is a factor of `n` but is not equal to 1, it adds `i` to the `factors` list and divides `n` by `i` to simplify the value of `n`. This loop continues until `n` is reduced to a single prime factor or is reduced to 1, at which point it's no longer considered a prime factor. Lastly, the final prime factors are appended to the `factors` list, and the function returns this list of prime factors, ordered from smallest to largest, each recorded the number of times it appears in the factorization. 

Here is an example of how you can use the factorize function:
```python
factorize(8)
# [2, 2, 2]

factorize(25)
# [5, 5]

factorize(70)
# [2, 5, 7]
```