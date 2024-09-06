```python
def truncate_number(n):
    return max(n - int(n), 0) if n.isdigit() else n
```

def test_truncate_number():
    assert truncate_number(3.5) == 0.0
    assert truncate_number("3.5") == 0.0
   
    ensure the said type assertion to run the test function and see if the function is working as expected.