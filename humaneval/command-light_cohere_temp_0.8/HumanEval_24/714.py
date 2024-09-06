```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer dividing n evenly, 
    including 1 if n is 1.
    """
    return n if n==1
    return n+1 if n%2==0
    return max(n-1, n+1) if n%2==1
    return 1
```