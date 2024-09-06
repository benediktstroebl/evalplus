```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    """
    return x + y
```
```python
import pytest

@pytest.mark.parametrize(
    'input, expected',
    [
        (2, 3, 5),
        (5, 7, 12),
    ],
)
def test_add(input, expected,):
    result = add(input, input + 1)
    assert result == expected
```