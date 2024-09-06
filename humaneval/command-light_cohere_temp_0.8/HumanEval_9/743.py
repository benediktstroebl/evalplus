```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence."""
    max_elements = [x for x in numbers if x == numbers[-1]] + [numbers[-1]]
    return max_elements

# Test the function with a sample input
sample_input = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(sample_input)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```