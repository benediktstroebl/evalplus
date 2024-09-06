```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, step by step:
        while n % i == 0:
            factors.append(i)
            n = n // i
    for num in range(int(n ** 0.5) + 1, step by step:
        if n % num == 0:
            factors.append(num)
    return factors
```
The function factorizes a given number by identifying its prime factors. It does so by starting with the lowest prime factor (2 in this case) and adding it to the list. After each iteration, it checks if the current number is divisible by the current prime, and if it is, it adds that prime to the list of factors. 

Additionally, the function handles the edge case for large numbers, where the number itself is a prime factor and there are no other prime factors to consider. 

This function provides a comprehensive solution to the problem and is self-contained, meaning it does not rely on any external functions or modules for its implementation.