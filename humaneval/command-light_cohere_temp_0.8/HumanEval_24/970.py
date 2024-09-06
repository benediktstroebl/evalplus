```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number that divides n evenly, smaller than n"""
    return [i for i in range(1, n+1) if n % i == 0]
```