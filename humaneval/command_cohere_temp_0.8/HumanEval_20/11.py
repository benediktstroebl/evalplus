```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return _get_closest_pair(left, right)


def _get_closest_pair(a, b):
    if (a - b) < 1e-6:  # adjust the threshold as needed
        return a, b
    elif abs(a - b) == min(abs(a - c) for c in numbers) or abs(a - b) == min(abs(b - c) for c in numbers):
        return a, b
    else:
        return _get_closest_pair(a, numbers[1]) if abs(a - numbers[1]) < 1e-6 else _get_closest_pair(numbers[0], b)
```

The test cases in the original problem are already thorough, exercising the function with different lengths of the input list, as well as different input numbers. Below is an example of adding additional tests covering edge cases and large input lists:
```python
def test_find_closest_elements():
    # Test cases from the problem statement
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)

    # Additional test cases
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0, 50.0, 31.3]) == (30.0, 31.3)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 1.5, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Edge cases
    assert find_closest_elements([10.0, 20.0, 30.0, 40.0]) == (20.0, 30.0)
    assert find_closest_elements([10.0, 20.0, 30.0]) == (20.0, 30.0)
    assert find_closest_elements([10.0, 20.0]) == (10.0, 20.0)

    # Large list
    large_numbers = [i / 10 for i in range(1000, 1100)]
    assert find_closest_elements(large_numbers) == (1000.0, 1010.0)
```