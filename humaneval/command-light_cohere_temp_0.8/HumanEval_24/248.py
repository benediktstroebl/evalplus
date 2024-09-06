```python
def largest_divisor(n: int) -> int:
    """
    Return the largest number that divides n exactly without a remainder.
    Return: n if it is a divisor of n
    otherwise find the smallest integer greater than n
    that divides evenly
    """
    if n == 2 or n == 1:
        return n
    if n <= 1:
        return 1
    else:
        return n // largest_divisor(n - 1)

# Unit tests
def test_largest_divisor():
    assert largest_divisor(1) == 1
    assert largest_divisor(2) == 2
    assert largest_divisor(3) == 3
    assert largest_divisor(4) == 4
    assert largest_divisor(5) == 5
    assert largest_divisor(6) == 6
    assert largest_divisor(7) == 7
    assert largest_divisor(8) == 8
    assert largest_divisor(9) == 9
    assert largest_divisor(10) == 10
    assert largest_divisor(15) == 5
```