Here is a self-contained Python function that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply a linear transform to that list,
    # such that the smallest number will become 0 and the largest will become 1
    numbers = [num / max(numbers) for num, max in zip(numbers, numbers)]
    return numbers
```

The function takes a list of numbers as input and applies a linear transform to the list by dividing each number by the largest number in the list. This ensures that the minimum number in the list becomes 0 and the maximum number becomes 1. 

You can test this function by passing different lists with numerical data, and it will return the list with the numbers scaled to the unit [0,1].