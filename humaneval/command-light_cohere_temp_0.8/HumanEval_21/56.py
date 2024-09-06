Here's a solution for the problem:

```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the numbers list, such that the smallest number becomes 0 and the largest becomes 1
    numbers = [x / 100 for x in numbers]
    return numbers
```

This function takes a list of numbers as input and returns a new list where each number has been divided by 100. The division is applied to each number in the list to ensure that the smallest number becomes 0 and the largest number becomes 1.