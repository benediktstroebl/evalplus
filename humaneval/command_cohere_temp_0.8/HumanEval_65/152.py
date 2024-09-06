```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:]+digits[:-shift] if len(digits) >= shift else digits[::-1]
```
This function takes an integer x and an integer shift as input, it shifts the digits of x to the right by shift and returns the result as a string. If the shift is greater than the number of digits, it returns the digits reversed. 

Here is an example usage of the function:
```python
circular_shift(12, 1) # Outputs "21"
circular_shift(12, 2) # Outputs "12"
circular_shift(5, -1) # Outputs "5"
circular_shift(1, 3) # Outputs "1"
```
```python
def test_circular_shift():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(5, -1) == "5"
    assert circular_shift(1, 3) == "1"
    assert circular_shift(123, -10) == "23"
    assert circular_shift(12345, 3) == "4521"
```
The test suite for this function is also provided, which checks the function against a variety of test cases.