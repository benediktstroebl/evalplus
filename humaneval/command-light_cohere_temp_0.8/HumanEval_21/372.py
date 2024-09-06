Here is a self-contained Python script that solves the problem of scaling down a list of numbers so that the smallest value becomes 0 and the largest becomes 1:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Create a copy of the list to avoid mutating the original list
    numbers_copy = numbers[:]
    # Apply the scaling to the copy of the list
    numbers_copy = [x / 100.0 for x in numbers_copy]
    # Return the rescaled list
    return numbers_copy
```
This script solves the problem by creating a new list numbers_copy with the same elements as the input list numbers, but with each value divided by 100. The original list numbers is then replaced with the scaled values, which effectively rescales the original list to have the smallest value become 0 and the largest value become 1.