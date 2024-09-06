```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, effectively leaving only the decimal part. 

To test this script, you can call the function with a float input, and the output will be the decimal part of the input. 

For example:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
or 
```python
truncate_number(12.56789)  # Expected: 0.56789
``` 
If the number entered is already integer, then the output will be 0, since there is no decimal part. 

For example:
```python
truncate_number(7)  # Expected: 0
``` 
You can also verify the behaviour for numbers close to integer boundaries, like 

```python
truncate_number(3.99999)  # Expect: 0.0001
``` 
or 
```python
truncate_number(10.1)  # Expect: 0.1
``` 
To verify if this function behaves as expected, you can employ tools like `pytest` for automated testing. Here is a code snippet for the corresponding test:
```python
import pytest

def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.56789) == 0.56789
    assert truncate_number(7) == 0
    assert truncate_number(3.99999) == 0.0001
    assert truncate_number(10.1) == 0.1
``` 
This test file contains one test function that tests the `truncate_number` function on five different inputs, verifying that the outputs match the expected values.