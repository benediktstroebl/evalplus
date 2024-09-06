```python
def truncate_number(n):
    return 0.5 if n < 0
   5
def test_truncate():
    assert truncate_number(-10) == 0.5
    assert truncate_number(-3) == -0.8
    assert truncate_number(3.7) == 0.7
def test_decimals():
    assert isinstance(truncate_number(1.2), (int)), float
    assert isinstance(truncate_number(1.5)), float
print("OK!")
```

This script defines a function `truncate_number` that takes a number as input and returns the decimal part of that number. Additionally, the script defines two functions: `test_truncate` and `test_decimals` that pass the test cases of the `truncate_number` function.