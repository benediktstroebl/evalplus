```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number less than n that divides it evenly.
    """
    test cases:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(10)
        5
        >>> largest_divisor(6)
        2
        >>> largest_divisor(12)
        4
    """
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b):
    while b:
        a, b = b, a % b
    return a
```