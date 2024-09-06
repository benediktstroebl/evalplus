```python
def largest_divisor(n: int) -> int:
    """Finds the largest divisor for the number n."""
    return next((d for d in range(1, n+1) if not divisible(n, d)), n)

def divisible(n: int, d: int) -> bool:
    """ Checks if divisor d divides n evenly."""
    return (n%d == 0) and d!=0

def test_largest_divisor():
    assert largest_divisor(15)==5
    assert largest_divisor(20)==5
    assert largest_divisor(5)==5
    assert largest_divisor(12)==4
    assert largest_divisor(10)==2
```