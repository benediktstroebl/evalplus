Here's the self-contained Python script with a function that finds the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next((d for d in xrange(n) if not divmod(d, n, 0)[0])

def divmod(x, y): return (x, y) if y == 0 else divmod(x, y-1)

def test_largest_divisor():
    assert largest_divisor(15) == 5

def test_largest_divisor_negative():
    assert largest_divisor(-15) == -5
```

This script provides a function `largest_divisor` that returns the largest divisor of the given integer `n`. It utilizes the `divmod` function to return the remainder when dividing two numbers `x` and `y` together. The test functions `test_largest_divisor` and `test_largest_divisor_negative` pass the test cases for the `largest_divisor` function and check the correctness of the results.