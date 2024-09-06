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

This code includes the `add` function, example usage, and a test suite that verifies the correctness of the `add` function. When the code is run, the tests will pass, confirming that the function behaves as expected.  This approach adheres to best practices in software development, providing a well-documented and tested function.