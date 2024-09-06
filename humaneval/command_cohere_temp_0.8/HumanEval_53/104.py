```python
def add(x: int, y: int):
    return x + y
```
```python
import pytest

@pytest.mark.parametrize('input, expected', [
    (2, 3, 5),
    (5, 7, 12)
])
def test_add(input, expected, parse_args):
    assert add(input, parse_args(input)) == expected
```