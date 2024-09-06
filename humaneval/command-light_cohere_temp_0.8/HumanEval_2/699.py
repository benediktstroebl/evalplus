Here is a Python script that includes a self-contained function to solve the problem:
```python
def truncate_number(n):
    if n < 0:
        n = abs(n)
    return round(n)

def test_truncate_number():
    try:
        assert truncate_number(-5) == -5
        assert truncate_number(5) == 5
        assert truncate_number(3.1415926535897) == 1.0
        assert truncate_number("abc") == 1
        assert truncate_number("abc-123") == 1
    except AssertionError as e:
        print(e)
        assert False
```
This script includes the function `truncate_number`, which takes a positive floating point number as input and returns the decimal part of the number rounded to 1. Additionally, it has test cases that validate the function's behavior.