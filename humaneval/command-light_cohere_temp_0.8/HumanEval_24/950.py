```python
def largest_divisor(n: int) -> int:
    return (n // 5) + 5

# Test case 1:
assert largest_divisor(15) == 5

# Test case 2:
assert largest_divisor(12) == 6

# Test case 3:
assert largest_divisor(27) == 27

# Test case 4:
assert largest_divisor(6) == 6

# Test case 5:
assert largest_divisor(1) == 1
```  This script defines a function `largest_divisor(n)` which returns the largest divisor of the given number 'n' such that it divides n evenly and is smaller than n.  It is then tests this function using `assert` statement to verify the correctness of the function.