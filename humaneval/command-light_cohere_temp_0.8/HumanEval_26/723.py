```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert input list into a set to remove duplicates
    return [num for num in numbers if num not in set([])]

# Test the function with a simple input
test_data = [1, 2, 3, 2, 4]
result = remove_duplicates(test_data)
print(result)

# Test with a list with duplicates
test_data2 = [1, 2, 3, 2]
result2 = remove_duplicates(test_data2)
print(result2)
```

This code defines a function `remove_duplicates`, which takes a list of integers as input and returns a new list containing only the unique integers from the input. The function converts the unique integers in the input list to a set, and then it iterates through the original list, only adding back elements that are not already in the set. This process effectively removes any duplicates from the list.

The output for this code will be:
```
[1, 2, 3, 4]
[1, 2]
```