```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transformation to the numbers list
    numbers = [x / 100.0 for x in numbers]
    return numbers

def test_rescale_to_unit(numbers):
    assert len(numbers) == 4
    assert all(isinstance(num, (int, float)) for num in numbers)
    assert all(num >= 0 for num in numbers)
    assert all(num <= 1 for num in numbers)
    assert sorted(numbers) == [0.0, 0.0, 0.0, 1.0])

print("Test succeeded")
```