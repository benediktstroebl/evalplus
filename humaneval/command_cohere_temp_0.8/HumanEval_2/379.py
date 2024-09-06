```python
def truncate_number(number):
    return number - int(number)
```
This function simply subtracts the largest integer that is less than `number` (the integer part of the decomposition described in the prompt). The result of the subtraction will be the residual fractional part of the number, achieving the desired output. 

To accompany the function, here is a test case that can be used to validate the functionality of the script:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(1.9999) == 0.9999
``` 

To run the test, you can add the test case and the function to a Python file and run the file. Here is an example:
```python
def truncate_number(number):
    return number - int(number)

def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(7.0) == 0.0
    assert truncate_number(1.9999) == 0.9999

if __name__ == "__main__":
    test_truncate_number()
```
Running this file with the command `python <filename>.py` will execute the test and display the test results. If you are curious as to how the code behaves for other numbers, add more test cases as needed.