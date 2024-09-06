```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[0]]

# Test cases
numbers1 = [1, 2, 3, 2]
numbers2 = [1, 2, 3, 4, 2]
numbers3 = [1, 2, 3, 4, 1, 5]

print("Test Case 1: Result:", remove_duplicates(numbers1))
print("")

print("Test Case 2: Result:", remove_duplicates(numbers2))
print("")

print("Test Case 3: Result:", remove_duplicates(numbers3))
print("")
```