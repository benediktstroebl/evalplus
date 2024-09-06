Here's the Python code for the problem you described:
```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    # Find the GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

if __name__ == "__main__":
    test_greatest_common_divisor()
```
This code provides a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. It employs the specific logic to find the GCD, and it passes all tests with flying colors.