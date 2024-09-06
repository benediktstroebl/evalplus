Here is a Python script that contains a self-contained function that calculates the largest divisor of a given number: 

```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer dividing the number evenly, 
    that is less than n.
    """
    def test_largest_divisor(n: int) -> None:
        """ Test driver function """
        result = largest_divisor(n)
        assert result == 5, f'Expected 5 but got {result}.'
        return result == 5
```