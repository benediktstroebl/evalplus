```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly and is less than n.
    """
    list of factors that are divisors of n are generated and the largest element is returned.
    return 1 + int(max(divisor for divisor in list(range(1, n)) & divisor == n))
```