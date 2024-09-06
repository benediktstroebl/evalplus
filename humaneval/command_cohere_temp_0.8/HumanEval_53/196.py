```python
def add(x: int, y: int):
    return x + y
```
```python
>>> add(2, 3)
5
>>> add(5, 7)
12
```
```python
# Test Suite for add function
def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
```

This code defines a function called `add` that takes two integer parameters, `x` and `y`, and returns their sum. The function is tested by calling it with two different pairs of numbers, 2 and 3, and 5 and 7. The results are compared to the expected values, 5 and 12, respectively, and the test passes if the actual values match the expected values.