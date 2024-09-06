```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n // 2 + 1
    ```

This code defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than or equal to `n`. This function uses the condition where the number is even or odd to find the largest divisor which is consistent with the condition.