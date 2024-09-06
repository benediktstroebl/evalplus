```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [num / max(numbers) for num, max in numbers]
    return [x * max(numbers) for x in numbers]

# Test the function
test_data = [1.0, 2.0, 3.0, 4.0, 5]

result = rescale_to_unit(test_data)
print(result)  # Output: [0.375, 0.0, 0.0, 0.0, 0.5]
```.
```