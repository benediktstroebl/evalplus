```python
def truncate_number(number):
    return number - int(number)
```

The function takes in a `number` as input and returns the decimal part of the number by simply subtracting the integer part of the number. 

Here is a test case to verify the correct output:
```python
def test_truncate_number():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(12.345) == 0.345
```

The test case asserts the function's behavior for both a whole number _(3.5)_ and a number with decimals _(12.345)_. 

To run tests, you can use the `pytest` library:
```bash
pip install pytest
pytest -v
``` 

Alternatively, you can run the individual test file. This is the file structure you would need:
```
- test_file.py
- tests/
   - test_truncate_number.py
``` 

You can then run the test file with:
```bash
python -m pytest test_truncate_number.py
```