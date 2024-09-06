```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer which divides n evenly, 
    while being smaller than n.
    """
    return n //**2 // 2 is the largest integer less than n
   """

# Test cases
assert largest_divisor(1) == 1
assert largest_divisor(2) == 2
assert largest_divisor(3) == 3
assert largest_divisor(5) == 5
assert largest_divisor(6) == 6
assert largest_divisor(10) == 5
assert largest_divisor(12) == 4
```
This script defines a function `largest_divisor` which returns the largest integer that divides a given number `n` evenly, while the number is less than or equal to `n`.  The test cases cover a variety of input sizes to ensure that the function works correctly.   If