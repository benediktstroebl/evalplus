```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of all numbers in the input array and iterates through the array to determine if each number is positive, negative, or zero, recording signs as 1, -1, or 0, respectively. Then it calculates the product of these signs and multiplies it by the sum of magnitudes. Ultimately it returns the desired result or None for an empty input.

Here's a test case to test the function:
```python
import numpy as np
import pytest

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([1, 2, 2, -4], -9),
        ([0, 1], 0),
        ([], None),
        (np.array([1, 2, 2, -4]), -9),
    ],
)
def test_prod_signs(test_input, expected):
    result = prod_signs(test_input)
    assert result == expected
```

This test uses the `pytest.mark.parametrize` decorator to create multiple test cases, which improves test efficiency. It provides different input arrays and the expected result for each, then asserts the function's output against these expected results.