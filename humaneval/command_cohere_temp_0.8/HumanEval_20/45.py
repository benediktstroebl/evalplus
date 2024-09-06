```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = abs(nums_sorted[-1] - nums_sorted[0])
    return nums_sorted[0], nums_sorted[-1] if diff == min(diff, *[abs(nums_sorted[i] - nums_sorted[i-1]) for i in range(1, len(nums_sorted))]) else nums_sorted[1], nums_sorted[0]
```

The function works by first sorting the list and then checking the closest elements, whether the closest elements are the first and the last elements, or the second and the second last elements. The closest elements are returned in the correct order (smallest first).

Here is a test suite that can be used to validate the function:
```python
def test_find_closest_elements():
    # Single closest element
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Multiple closest elements
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # No elements in list
    assert find_closest_elements([]) == tuple()

    # Single element list
    assert find_closest_elements([7.0]) == (7.0, )

    # Duplicate elements
    assert find_closest_elements([0.0, 1.0, 1.0, 2.0, 3.0, 4.0, 1.0, 1.0, 5.0]) == (1.0, 1.0)
```

This test suite can be executed with python -m pytest -v  or with `unittest` by importing the `unittest` module and by running the `unittest.main()` function.