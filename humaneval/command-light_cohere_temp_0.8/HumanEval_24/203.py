```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number which divides n exactly
    """
    return [i for i in range(1, int(n**0.5)+1) if n % i == 0]
```