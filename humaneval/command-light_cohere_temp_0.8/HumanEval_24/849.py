```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number smaller than n, 
    that divides n evenly.
    """
    test case: 
        assert 1 == largest_divisor(1), "Error: 1 is not divisible by 1"
    assert 2 == largest_divisor(2), "Error: 2 is not divisible by 2"
    assert 3 == largest_divisor(3), "Error: 3 is not divisible by 3"
    assert 4 == largest_divisor(4), "Error: 4 is not divisible by 4"
    assert 5 == largest_divisor(5), "Error: 5 is not divisible by 5"
    assert 6 == largest_divisor(6), "Error: 6 is not divisible by 6"
    assert 7 == largest_divisor(7), "Error: 7 is not divisible by 7"
    assert 8 == largest_divisor(8), "Error: 8 is not divisible by 8"
    assert 9 == largest_divisor(9), "Error: 9 is not divisible by 9"
    assert 10 == largest_divisor(10), "Error: 10 is not divisible by 10"
    return 5
```