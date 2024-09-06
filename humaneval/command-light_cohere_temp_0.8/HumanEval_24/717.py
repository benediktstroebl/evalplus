Here is a Python script that contains a self-contained function that calculates the largest divisor of a given number:

```python
import math
def largest_divisor(n: int) -> int:
    # Initialize the largest divisor found
    largest_divisor = 1
    while n % largest_divisor == 0:
        largest_divisor *= largest_divisor
    n //= largest_divisor
    return largest_divisor
```

This code defines a function `largest_divisor` which takes an integer `n` as input and returns the largest divisor of `n`. It uses a loop to find the largest number that divides `n` evenly, smaller than `n`, and returns the largest divisor. 
This is a self-contained function that has no external dependencies and can be easily tested.