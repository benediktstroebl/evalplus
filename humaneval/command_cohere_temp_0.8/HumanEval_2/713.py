```python
def truncate_number(number):
    return number - int(number)
```

The function takes in a `number` as an input and returns the decimal part of the number by simply subtracting the integer part of the number. 

Here is a test case to verify the correct output:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.345) == 0.345
```

The test case uses the `assert` statement to see if the output of the `truncate_number()` function is equal to the desired output. 

To run the code, you can save the code above in a Python file (e.g., `truncate_number.py`) and then execute the file in your command line using `python truncate_number.py`. Alternatively, you can copy and paste the code into a Python interpreter in your command line.