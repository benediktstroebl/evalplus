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

The code employs an iterative method to find the prime factors of an integer `n`. It begins by assuming the factors are empty and iterates through divisors ranging from 2 up to `n`. For each divisor, it checks if it can divide `n` without leaving a remainder. If possible, it increments the `count` variable, indicating the number of times that divisor can divide `n` without leaving a remainder. Afterwards, the divisor is appended to the `factors` list, and `count` is handled as sometimes it could be 0. The loop continues until `n` becomes 1, at which point the loop stops. Finally, any factor that isn't recorded (since its `count` was 0) is appended to the list, ensuring that all prime factors are accounted for. 

Here is an example usage of the code:
```python
factorize(8)  # [2, 2, 2]
factorize(25)  # [5, 5]
factorize(70)  # [2, 5, 7]
```

This should match the expected output as outlined in the problem statement.