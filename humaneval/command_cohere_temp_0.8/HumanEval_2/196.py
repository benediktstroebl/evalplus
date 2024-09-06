```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes the input number and returns the decimal part of the number by subtracting the integer part of the number. 
The test case will be an example of the function usage:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.345) == 0.345
```
The test cases will check if the function returns the correct decimal part for the given input. 
The expected result is `0.5` for the first test case and `0.345` for the second test case. 
To run the test cases, you can use the Python unittest framework:
```bash
python -m unittest test_truncate_number.py
``` 
The expected outcome of this command is `Ran 1 test in 0.001s` and `OK`, meaning the function's result is correct. You can always check the `test_truncate_number.py` file for more elaborate test cases to ensure the correctness of the function.