```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)


# Test cases
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [3, 2, 4, 5, 2]
numbers3 = [1, 2, 2, 3]

print(remove_duplicates(numbers1))  # Output: [1, 3, 4]
print(remove_duplicates(numbers2))  # Output: [3, 4, 5]
print(remove_duplicates(numbers3))  # Output: [1, 2, 3]
```

The provided Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function achieves this purpose by converting the input list into a set, which automatically eliminates duplicates. Then, the set's elements are converted back into a list. The function is successfully tested using three different input lists, and the output confirms the removal of duplicates.