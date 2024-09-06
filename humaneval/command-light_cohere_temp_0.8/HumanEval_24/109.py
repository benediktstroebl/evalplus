```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This code defines a function called `largest_divisor` that takes an integer n as input and returns the largest integer that divides n evenly, smaller than n. The function uses the process that checks if the number is even, then it returns n divided by 2, otherwise, it returns n plus 1.