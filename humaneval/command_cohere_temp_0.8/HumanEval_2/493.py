```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. 

To test this function, here is a test case that can be used:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(12.83) == 0.83
    assert truncate_number(0.01) == 0.0
    assert truncate_number(101.23) == 0.23
``` 

To run this test, you can write `test_truncate_number()` in the Python interpreter or run the `.py` file with the test code with `python test.py`. 

Please note that the tests assume the function `truncate_number()` is defined in a file named `test.py` and it has the `assert` statements to verify the expected output. 
If you want to test functions in the Python interpreter, you can use the `>>>` prompt, which is designed specifically for testing functions in the Python interpreter. If you have any further questions, please let me know!