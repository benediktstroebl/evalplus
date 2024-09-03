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

This code snippet includes the `add` function, example usage, and a test suite that verifies the correctness of the `add` function. The function takes two integers `x` and `y` and returns their sum. The test suite confirms that the function appropriately adds the numbers. This comprehensive approach ensures the functionality of the addition operation.