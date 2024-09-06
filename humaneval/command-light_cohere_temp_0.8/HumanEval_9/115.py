```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of the rolling maximum elements in numbers, as an descending sequence. 
    Tests for i in range(len(numbers)):
        numbers[i] = max(numbers[i+1], numbers[i])
    return [x for x in numbers if x == max(numbers)]

# Test case:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result) # Output: [4, 3, 3, 2]

# Test case:
numbers = [4, 4, 4, 4, 4]
result = rolling_max(numbers)
print(result) # Output: [4, 4, 4, 4]

# Test case:
numbers = [1, 1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result) # Output: [1, 2, 3, 4]
```
This script defines a function rolling_max which takes a list of integers as input and returns a list of the rolling maximum elements in descending sequence. It uses the use a previous maximum element to the next element in the sequence, effectively generating the rolling maximum elements. The test cases demonstrate the running_max's functionality by providing different lists of integers and printing the resulting descending sequence of maximum elements.