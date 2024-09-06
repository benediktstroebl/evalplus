Here's the self-contained Python script that defines a function to find the largest divisor of a given number: 

```python
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    max_divisor = n - 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            max_divisor = max(max_divisor, i)
    return max_divisor
```

This script defines a function called `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`. The function first handles the base case where `n` is less than or equal to 1 by returning `n`. The function then initializes `max_divisor` to `n - 1`. Then, it iterates from 2 up to the square of the floor of `n` divided by 2, checking if `n` is divisible by each integer in this range. The function returns the the maximum divisor found so far or the largest divisor of `n`.