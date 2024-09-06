```python
def multiply(a, b):
    """Returns the product of the unit digits of the inputted integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function str(a)[-1] converts the input number into a string, then accesses the last character to capture the unit digit. Repeating this process for both inputs and multiplying the unit digits yields the desired result. 

Here is a test drive code to verify the functionality of the update:
```python
def test_multiply():
    assert multiply(12, 14) == 2
    assert multiply(19, 28) == 72
    assert multiply(2020, 1851) == 0
    assert multiply(14, -15) == 20

test_multiply()
```

The test_multiply function executes multiple tests to cover different cases such as positive, negative, and zero numbers. The assert statements check if the result from the multiply function for a given input matches the expected output. When the code is run, the test_multiply function is called and the assert statements will fail if the multiply function returns anything other than the expected outputs.