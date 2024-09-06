```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 

To test this function, here is a sample test case:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.9872) == 0.9872
    assert truncate_number(123123.123) == 0.123
``` 
The tests ensure that the function correctly identifies and returns the decimal portion of the input number. 

To run the tests in a Python script, the following is a sample command line instruction: 
```python
python test_truncate_number.py
``` 
This will run the tests and provide an output of the test results.