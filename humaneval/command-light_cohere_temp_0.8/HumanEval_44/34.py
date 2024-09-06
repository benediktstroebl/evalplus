```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    Returns string representation after conversion.
    base numbers less 10."""
    return '{:b}'.format(x, base)

def test_change_base():
    assert change_base(8, 3) == '22', "Test 1 failed"
    assert change_base(5, 2) == '10', "Test 2 failed"
    assert change_base(7, 2) == '111', "Test 3 failed"

if __name__ == "__main__":
    test_change_base()
```
This code defines a function `change_base` that converts a number to a specified base. The function takes two parameters: the number `x` to be converted and the base `base` to which it should be converted. The function then returns the string representation of the number in the specified base.

The `test_change_base` function contains asserts that check the correctness of the `change_base` function. The script runs the `test_change_base()` function to execute the test. 
The test will pass if the function is working correctly.