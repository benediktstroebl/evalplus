```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    return 0.5 * a * h
```

To ensure the function is robust, add tests that cover different cases. Test scenarios can include:
- Valid inputs: Test with 'a' and 'h' as positive numbers.
- Negative numbers.
- Zero.
- None.

Here's an example of how to use pytest to incorporate these into the script:
```python
# test_triangle_area.py
import pytest
from triangle_area import triangle_area

@pytest.mark.parametrize(
    "side,height,expected",
    [
        (5, 3, 7.5),  # Basic example from docstring
        (0, 0, 0),  # Handle zeros
        (-5, 7, -2.5),  # Negative numbers
        (None, 10, None),  # Handle None inputs
    ]
)
def test_triangle_area(side, height, expected):
    result = triangle_area(side, height)
    assert result == expected
```

In this test suite, the `@pytest.mark.parametrize` decorator creates multiple test cases by auto-generating test functions with different inputs. This helps streamline the process and makes it easier to add more test cases in the future.

Run the tests using `python -m pytest test_triangle_area.py`.

This approach ensures that the function behaves as expected in different scenarios and helps to validate its correctness, ensuring its resilience in handling various input types.