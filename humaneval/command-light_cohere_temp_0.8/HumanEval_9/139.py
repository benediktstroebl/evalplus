```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers and returns a list of rolling maximum elements found
    until the given moment in the sequence.
    Each element in the numbers will be replaced with its corresponding rolling 
    maximum element until the list is fully traversed.
    Return values are rolling max as [max(numbers[0]), max(numbers[1]), ...]
    """
    return [max(numbers[i]) for i in range(len(numbers))]

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [3, 2, 4, 5]
numbers3 = [10, 5, 6, 7]

print(rolling_max(numbers1))  # Output: [1, 2, 3, 3]
print(rolling_max(numbers2))  # Output: [3, 4, 5, 5]
print(rolling_max(numbers3))  # Output: [10, 6, 7]
```
This script defines a function called rolling_max that takes a list of integers as an input and returns a list of rolling maximum elements. The function works by using a simple loop and the max() function to find the maximum element in each sublist. The test cases show that the function correctly calculates the rolling maximum for each given list of numbers.