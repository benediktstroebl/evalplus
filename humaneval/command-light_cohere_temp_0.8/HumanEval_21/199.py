Here's a self-contained Python script that solves the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [n / 100.0 for n in numbers]
    return numbers


def test_rescale_to_unit(numbers):
    assert len(numbers) == 2, "Input list must have at least two elements"
    return rescale_to_unit(numbers)


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0.0]
assert test_rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 0.75, 1.0])
```