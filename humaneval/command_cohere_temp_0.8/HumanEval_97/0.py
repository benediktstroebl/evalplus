```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function str(a)[-1] converts the integer `a` to a string and extracts its last character, which is its unit digit. Likewise, the same operation is performed on b. Then the unit digits are multiplied and returned as an integer using the int() function. This solution optimally uses string manipulation and avoids unnecessary complexities.

Here is a test suite that verifies that the function correctly solves the problem:
```python
def test_multiply():
    # Test case 1
    assert multiply(148, 412) == 16
    
    # Test case 2
    assert multiply(19, 28) == 72
    
    # Test case 3
    assert multiply(2020, 1851) == 0
    
    # Test case 4
    assert multiply(14, -15) == 20

test_multiply()
```
The test suite contains different input values and expects the output to match the 'Examples' part of the problem statement.