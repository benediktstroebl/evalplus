```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = nums_sorted[1] - nums_sorted[0]
    for i in range(1, len(nums_sorted)):
        curr_diff = nums_sorted[i] - nums_sorted[i - 1]
        if curr_diff < diff:
            diff = curr_diff
    return nums_sorted[0], nums_sorted[1]
```

The function `find_closest_elements` works by first sorting the input list of numbers. Then, it computes the difference between subsequent elements in the sorted list, and keeps track of the smallest found difference. Finally, it returns the first and the second element of the list, which correspond to the smallest difference found. The function returns those two elements.

Here is a simple test suite that can be used to verify the correctness of the function:
```python
def test_find_closest_elements():
    # Example 1:
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
    expected_result = (2.0, 2.2)
    result = find_closest_elements(numbers)
    assert result == expected_result

    # Example 2:
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
    expected_result = (2.0, 2.0)
    result = find_closest_elements(numbers)
    assert result == expected_result

    # Edge case:
    numbers = [10.0, 20.0, 30.0]
    expected_result = (10.0, 20.0)
    result = find_closest_elements(numbers)
    assert result == expected_result

test_find_closest_elements()
```

The test suite checks correct behavior against two examples and one edge case, it should be adapted to cover a diverse range of inputs to ensure that the function behaves as expected.