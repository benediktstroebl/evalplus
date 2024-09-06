```python
def truncate_number(number: float) -> float:
    return 0.5 if number <= 1.5 else number0.0
```

def test_truncate():
    assert truncate_number(3.5) == 0.0
    assert truncate_number(-3.5) == -0.0

def test_negative():
    assert truncate_number(-5.0) == 0.0

def test_large_positive():
    assert truncate_number(10.0) == 1.0

def test_high_digits():
    assert truncate_number(15.3) == 1.0
```