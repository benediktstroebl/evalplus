Here's the code:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the Mean Absolute Deviation
    mad = sum((x - mean) ** 2 for x, mean in zip(numbers, numbers[::mean])) ** 0.5 / len(numbers)
    return mad


# Test cases
test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
assert mean_mean_absolute_deviation(numbers=test_mean_absolute_deviation([1.0, 2.0, 3.0, 4])) == 0.0


test_mean_absolute_deviation([2.0, 2.0, 2.0])
assert mean_mean_absolute_deviation(numbers=test_mean_absolute_deviation([2.0, 2.0, 2])) == 0.0


test_mean_absolute_deviation([1.0, 2.0, 3.0])
assert mean_mean_absolute_deviation(numbers=test_mean_absolute_deviation([1.0, 2.0, 3])) == 0.0


test_mean_absolute_deviation([0.0, 4.0, 4.0])
assert mean_mean_absolute_deviation(numbers=test_mean_absolute_deviation([0.0, 4.0, 4])) == 0.0


test_mean_absolute_deviation([1.0, 3.0, 2.0])
assert is_mean_absolute_deviation(numbers=test_mean_absolute_deviation([1.0, 3.0, 2])) == 0.0


test_mean_absolute_deviation([0.0, 4.0, 4])
assert is_mean_absolute_deviation(numbers=test_mean_absolute_deviation([0.0, 4.0, 4]))


test_mean_absolute_deviation([1.0, 2.0])
assert is_mean_absolute_deviation(numbers=test_mean_absolute_deviation([1.0, 2.0]))


test_mean_absolute_deviation([2.0, 1.0, 1.0])
assert is_mean_absolute_deviation(numbers=test_mean_absolute_deviation([2.0, 1.0, 1]))


test_mean_absolute_deviation([3.0, 3.0, 2.0])
assert is_mean_absolute_deviation(numbers=test_mean_absolute_deviation([3.0, 3.0, 2]))

test_mean_absolute_deviation([4.0, 2.0, 1])
assert is_mean_absolute_deviation(numbers=test_mean_absolute_deviation([4.0, 2.0, 1]))

test_mean_absolute_deviation([5.0, 2.0, 1])
assert is_mean_absolute_deviation(numbers=test_mean_absolute_deviation([5.0, 2.0, 1]))

test_mean_absolute_deviation([2.0, 6.0, 4])
assert is_mean_absolute_deviation(numbers=test_mean_absolute_deviation([2.0, 6.0, 4]))

test_mean_absolute_deviation([0