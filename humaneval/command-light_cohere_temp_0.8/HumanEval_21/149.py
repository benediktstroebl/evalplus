```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    return [num / min(numbers) if num < min(numbers) else 1 - num / max(numbers) else num for num in numbers]

# Test case:
numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0]
print_in = rescale_to_unit(numbers)

# Test case 2:
numbers = [0.0, 0, 0, 0]
print_in = rescale_to_unit(numbers)
```