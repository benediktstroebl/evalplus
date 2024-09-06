```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number divisible by n that is less than n.

    Example: n = 16 
    a = 4
    b = 2
    c = 3
    while a <= n:
        while n % a == 0:
            n /= a
        a = a + 1 
    while n <= b:
        if n % b == 0:
            n /= b
        b = b + 1
    if n > b:
        c = b + 1 
    return min(c, n)
```