```python
def add(x: int, y: int):
    return x + y
```
```python
>> add(2, 3)
5
>> add(5, 7)
12
```
```python
# Test Suite for add function
def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
```

This code includes the function `add` and a test suite that ensures it behaves as expected. The function returns the sum of two integers, and the test suite validates that it produces the correct results for various input combinations.