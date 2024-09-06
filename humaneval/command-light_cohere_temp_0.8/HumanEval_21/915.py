```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation
    numbers = [num / max(numbers) for num in numbers]
    return numbers


# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 0.0]
numbers = rescale_to_unit(numbers)  # Should return [0.0, 0.0, 0.0, 0.0]
print(numbers)  # Output: [0.0, 0.0, 0.0, 0.0]
assert is_sequence(numbers) == [0.0, 0.0, 0.0, 0.0])

assert is_sequence([1.0 / max(numbers) for num in numbers] for numbers in [1.0, 2.0, 3.0, 4.0, 5.0, 0])

numbers = [0.0, 0.0, 0.0, 6.0, 0]
numbers = rescale_to_unit(numbers)  # Should return [0.0, 0.0, 0.0, 0]
print(numbers)  # Output: [0.0, 0.0, 0.0, 0]
assert is_sequence(numbers) == [0.0, 0.0, 0, 0])
```