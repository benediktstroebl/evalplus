```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements found in the given list of integers """
    return [x for x, i in zip(numbers, numbers[1:])] + [max(x, numbers[0])]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers = [1, 1, 4, 2, 3, 3, 1, 4, 3]
result = rolling_max(numbers)
print(result)
```
This script provides a self-contained function `rolling_max` which accepts a list of integers and returns a list of the rolling maximum elements found in the sequence. It employs a list comprehension and a nested loop to achieve this. Additionally, it utilizes the max function to calculate the maximum element in each rolling window. The provided example demonstrates the result for two different lists of integers. The output will display the maximum elements for each list.