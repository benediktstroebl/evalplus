Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [num / max(numbers) for num in numbers]
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1]. The function simply divides each number in the list by the maximum number in the list. This ensures that the largest number will become 1 and the smallest (zero) will become 0, thus scaling the list to the unit interval.

Here's an example usage of the function provided:
```python
# Test the function with a sample input
sample_input = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(sample_input))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This will produce the expected output, scaling the list such that the smallest number (1) becomes 0 and the largest (5) becomes 1.