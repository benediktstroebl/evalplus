```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]


# Example of how to use the function:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers2 = [5, 5, 5, 6, 6]
result2 = remove_duplicates(numbers2)
print(result2)  # Output: [5, 6]
```