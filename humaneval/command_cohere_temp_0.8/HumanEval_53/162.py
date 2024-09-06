```python
def add(x: int, y: int):
    return x + y
```
```python
# Test add function
import pytest

@pytest.mark.parametrize(
    "test_input, expected",
    [
        (2, 3, 5),
        (5, 7, 12),
    ],
)
def test_add(test_input, expected):
    result = add(test_input, y=test_input)
    assert result == expected
```
This code defines a function called add which takes two integers x and y as arguments and returns their sum. It then passes different test cases which verify that the function works correctly and returns the expected outputs.