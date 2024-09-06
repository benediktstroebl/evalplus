```python
def add(x: int, y: int):
    return x + y
```
```python
# Test add function
import pytest

@pytest.mark.parametrize('test_input, expected', [
    (2, 3, 5),
    (5, 7, 12)
])
def test_add(test_input, expected):
    result = add(test_input, test_input)
    assert result == expected
```
In the code above, we define a parameterized test in pytest that takes in two inputs, `test_input` and `expected`, and checks whether the `add` function returns the expected value. This is done to validate the correctness of the `add` function against known inputs.