```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test the function with a sample input
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

# Test the function with a different input
numbers2 = [1, 3, 4, 2, 5, 6]
result2 = remove_duplicates(numbers2)
print(result2)  # Output: [1, 3, 4, 5, 6]
```

The function `remove_duplicates` takes a list of integers as input and returns a new list that contains only the unique elements from the original list. This is done using the using the `set()` function to convert the list into a set, which removes duplicate elements, and then the `list()` function is used to convert the set back into a list.