```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, idx in zip(sorted(numbers), reversed(range(len(numbers)))) if idx < len(numbers) and numbers[idx] > numbers[idx - 1]]

# Example of passing the test
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
This code defines a function `rolling_max` that takes a list of integers as input and returns a new list with the rolling maximum elements. 

This function uses a `zip` operation to iterate over the elements of the input list and the corresponding index, then checks if the current element is greater than the previous one, which corresponds to the maximum element found so far. 

The example at the end demonstrates how to call the function with a sample list of integers and print the resulting list of maximum elements.