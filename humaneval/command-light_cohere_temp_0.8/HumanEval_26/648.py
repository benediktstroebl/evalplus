```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test the function
numbers = [1, 2, 3, 2, 4, 2, 1]
result = remove_duplicates(numbers)
print(result)

numbers = [1, 2, 3, 4, 5, 6, 7]
result = remove_duplicates(numbers)
print(result)

numbers = [2, 2, 4, 2, 6, 2]
result = remove_duplicates(numbers)
print(result)
```
The script defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The test cases demonstrate the actual results for different lists. The set function is used to create a unique list of integers. The unique elements are then returned by the function.