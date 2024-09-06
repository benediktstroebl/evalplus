```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest number that divides n evenly, smaller than n.
    """
    numbers from 1 to n // 2 do not divide n evenly
    divisor = 5
    while any(num // n == 0 for num in range(1, n+1) ):
        divisor -= 1
    return divisor
```