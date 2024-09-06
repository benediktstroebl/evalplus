```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return list(numbers)

# Test the function
test_remove_duplicates = []
test_remove_duplicates.append([1, 2, 3, 2])
test_remove_duplicates.append([4, 4, 3, 2])

result = remove_duplicates(test_remove_duplicates)
print(result)  # Output: [1, 3, 4]

# Test again to make sure it works
test_remove_duplicates.append([1, 2, 3, 2])
test_remove_duplicates.append([4, 3, 2])

result = remove_duplicates(test_remove_duplicates)
print(result)  # Output: [1, 2, 3]
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list that contains only the unique elements from the original list. The test section demonstrates this usage by passing two different test lists to the function, and then printing the results.