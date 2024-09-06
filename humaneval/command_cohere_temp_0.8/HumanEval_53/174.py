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

This code consists of two scripts: the `add` function and a `test_add` function to verify the correctness of the `add` function. 

1. The `add` function takes two integers `x` and `y` as inputs and returns their sum. It is a straightforward addition operation.
2. The `test_add` function is a test suite to validate the correctness of the `add` function. It employs `pytest.mark.parametrize` to wrap multiple test cases within a single function. Each test case includes two placeholders `test_input` and `expected`, representing the input to the `add` function and the expected output respectively. 

In each test case, the `add` function is invoked with `test_input`, and its result is compared against `expected` using the `assert` statement. If all tests pass without raising an assertion error, it indicates that the `add` function complies with the expected behavior.