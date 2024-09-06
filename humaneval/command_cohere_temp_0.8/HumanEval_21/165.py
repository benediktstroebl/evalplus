Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [num / max(numbers) for num in numbers]
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1]. The function simply divides each number in the list by the maximum number in the list. This approach ensures that the largest number in the list becomes 1, and the smallest number becomes 0, preserving the relative relationships between the numbers.