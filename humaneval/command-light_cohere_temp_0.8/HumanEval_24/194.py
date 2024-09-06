```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n` which is smaller than `n`. This function utilizes the condition that the largest divisor of a number divisible by 2 is either 2 or the number itself plus 1, to achieve this.