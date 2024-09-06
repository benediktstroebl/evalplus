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
# Test suite with successful tests
def test_add_positive_results():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
```
```python
test_add_positive_results()
```