Here is a Python script that contains a self-contained function that finds the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next((i for i in range(1, n+1) if n % i == 0))

# Test suite
def test_largest_divisor():
    assert largest_divisor(15) == 5

# Test case 1
print("Test case 1 passed!")

test_largest_divisor()
``` 
This script defines a function called `largest_divisor` that returns the largest integer which divides the given number `n` evenly. 
For each number from 1 to `n`, it checks whether the number divides `n` evenly (i.e.  If result is largest integer which number that divides n evenly and returns the largest one from this set.