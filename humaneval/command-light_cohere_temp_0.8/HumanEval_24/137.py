```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that evenly divides the number n, 
    without being equal to n.
    """
    algorithm:
        while any(divisor == n) or divisor > 1:
            divisor = divisor - 1
        return divisor
    """

# Testing the function
def test():
    assert largest_divisor(15) == 5
    assert largest_divisor(25) == 5
    assert largest_divisor(7) == 1
    assert largest_divisor(8) == 2
    assert largest_divisor(10) == 5
    assert largest_divisor(16) == 4
```