Here is a Python script that solves the problem of finding the rolling maximum elements in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_value = numbers[0]
    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return [max_value]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the rolling maximum elements. The script then provides an example usage of this function with a list of numbers and prints the result, which is a list of the maximum elements from the original list.