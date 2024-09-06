```python
def largest_divisor(n: int) -> int:
    """Finds the largest number which divides n exactly and is smaller than n."""
    return n if n % 2 == 0 else n+1
    ```
This code defines a function `largest_divisor` which takes an integer `n` as input and returns the largest integer that divides `n` exactly and is smaller than n. The function uses the fact to determine whether the input number is even or odd, and it returns the respective value accordingly.