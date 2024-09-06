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
def test_add(input, expected, merge_fixture):
    actual = add(input, merge_fixture)
    assert actual == expected
```

This code defines a function called `add` that takes two integers (`x` and `y`) as input and returns the sum of these numbers. It uses the `pytest` framework to define unit tests for the `add` function that verifies whether the function correctly computes the sum of various input combinations. 

The code ensures that the `add` function performs addition as expected, making it a useful and reliable building block for future applications that require basic numerical computations.