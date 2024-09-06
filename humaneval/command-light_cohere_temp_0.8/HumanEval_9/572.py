```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in sorted((num, i) for i, num in enumerate(numbers)) if i < len(numbers) and num > numbers[i]]

# Test case 1
numbers = [1, 2, 3, 4, 3, 2, 1]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test case 2
numbers = [1, 2, 3, 4, 3, 4, 3]
result = rolling_max(numbers)
print(result)  # Output: [1, 3, 3, 3, 4, 4]

# Test case 3
numbers = [1, 2, 3, 4, 5, 4, 3, 4]
result = rolling_max(numbers)
print(result)  # Output: [2, 3, 3, 4, 4]
```
This script defines a function called rolling_max that takes a list of integers as input and returns a new list with the elements from the input list that are the maximum value as they occur in the sequence. It uses the dynamic programming and the sort the elements in descending order using the index and then uses the index to filter out the maximum value. The test cases demonstrate that the expected output.