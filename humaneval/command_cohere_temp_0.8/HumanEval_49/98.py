Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the modp function which takes in two integers n and p, and returns 2^n modulo p. This is accomplished by using the built-in function pow which calculates (2, n) modulo (p, ), respectively.

To test this function, you can uncomment the respective lines and execute the corresponding tests:
```python
# Test suite
import random

def test_modp():
    # Basic tests
    assert modp(0, 101) == 1
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2

    # Some more tests
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

    # Random tests
    for _ in range(5):
        n = random.randint(0, 10000) // 2
        p = random.randint(1, 10000)
        assert modp(n, p) == pow(2, n, p)

# Execute the test suite
test_modp()
```
```
NOTE: The code includes a test suite with a variety of tests, you can run this test suite to verify the correctness of the function.
```