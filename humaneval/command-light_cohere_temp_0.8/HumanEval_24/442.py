```python
def largest_divisor(n: int) -> int:
    """Finds the largest number that divides n evenly, smaller than n"""
    return int((n + 1) / 2)  # O(log2(n)) time
```