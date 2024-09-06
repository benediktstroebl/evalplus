```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # transform the numbers
    return [min(x, y) / (max(x, y) - min(x, y)) for x, y in zip(numbers)]

# test the function
test_numbers = [0.1, 0.5, 0.5, 0.0, 0.0, 5.0]
test_rescale_to_unit(test_numbers)

# expected output: [0.25, 0.0, 0.0, 0.0]
```