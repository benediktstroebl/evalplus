```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 
The test cases will look as follows:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.345) == 0.345
    assert truncate_number(123.7) == 0.7
    assert truncate_number(2.0) == 0.0
    assert truncate_number(1.1) == 0.1
``` 
The overall time complexity of the function is O(1). The function operates on one input element and performs a simple mathematical operation to arrive at the output.

The space complexity is O(1). Except for the stack space required to execute the function, no extra space is utilized.