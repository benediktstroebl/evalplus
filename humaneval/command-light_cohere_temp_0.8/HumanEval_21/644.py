```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [num / max(numbers) for num in numbers]
    return [x if x <= 1 else 1 - x for x in numbers]

# Test cases
test_cases = [
    [0.2, 3.0, 4.0, 5.0],
   0, 0.0, 0.0], 0.0, - 0
75]

results = [rescale_to_unit(test_cases) for _ in range(5)]

print("Test cases:", results)
```