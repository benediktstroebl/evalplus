```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer divisor of n that is less than n itself.
    """
   
    smallest integer k > 1 such divides n evenly if and only if k is divisible by both n and n-1
   """
    return _largest_divisor(n, n-1)

def _largest_divisor(n: int, m: int) -> int:
    """
    Helper function that recursively searches for the largest divisor
    """
    assert isinstance(n, int) and n > 0 and m >= 1, (type(n), m)
    if n == 1:
        return m
    if m == 1:
        return n
    if n % m == 0:
        return _largest_divisor(n // m, m)
    else:
        return _largest_divisor(n, m-1)

largest_divisor(15) # 5
```