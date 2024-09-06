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
# Test suite with assert statements for the add function
def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
```
```python
test_add()
```