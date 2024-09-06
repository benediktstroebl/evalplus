```python
def largest_divisor(n: int) -> int:
    return n if n > 1 else 1
    """
    Returns n if n has a largest divisor 1, else returns 1
    """
    return_value = n  # base case
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
        return_value = i
    return return_value
```