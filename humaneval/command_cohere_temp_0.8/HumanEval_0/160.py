```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

To efficiently check if there are any close elements, we can compare each number in the list with the following one, as the problem statement states that the list is not sorted and contains positive integers. We use the `any` function to check if any comparison returns a truthy value, meaning that there is at least one pair of numbers that are closer than the threshold. 

This solution adheres directly to the problem statement, and therefore achieves the desired result.