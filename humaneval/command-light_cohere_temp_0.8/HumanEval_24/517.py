```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)
```
This Python function named largest_divisor takes an integer n as input and returns the largest integer that divides n evenly, ensuring the result is greater than or equal to 1. It achieves this by utilizing the max function with the condition n >= 1 to efficiently find the maximum integer less than n.