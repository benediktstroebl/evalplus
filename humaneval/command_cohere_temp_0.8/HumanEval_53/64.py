```python
def add(x: int, y: int):
    return x + y
```
```python
# Test add function
import pytest

@pytest.mark.parametrize('input, expected', [
    (2, 3, 5),
    (5, 7, 12)
])
def test_add(input, expected):
    result = add(input, input + 1)
    assert result == expected
```