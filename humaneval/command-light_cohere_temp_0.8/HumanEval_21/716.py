```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [n / 100.0 for n in numbers]
    return numbers

def test_rescale_to_unit(numbers):
    assert len(numbers) == 3, "Input list should have at least two elements"
    for i in range(2):
        assert numbers[i] >= 0.0 and numbers[i] > 0.0, "The smallest number should become 0 and the largest number should become 1"
    assert numbers[0] + numbers[1] == 1.0, "The product of the sum of the first two numbers should be 1"
    assert numbers[1] * numbers[2] == 1.0, "The product of the product of the first and second numbers should be 1"
    assert numbers[0] + numbers[2] == 0.0, "The sum of the first two numbers should be 0"
    assert numbers[0] * numbers[1] == 2.0, "The product of the first two numbers should be 2"
    assert numbers[0] ** min(numbers[1], numbers[2]) == 1.0, "The exponent should be the smallest of the two numbers"
```