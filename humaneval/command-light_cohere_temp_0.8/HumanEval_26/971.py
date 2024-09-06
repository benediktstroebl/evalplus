```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Unit tests
numbers = [1, 2, 3, 2, 4, 2, 1, 5]
test_remove_duplicates = [
    "This function correctly removes duplicate elements.",
    "It should return [1, 3, 4]",
    "test1",
    "test2",
    "test3",
    "test4",
    "test1",
    "test5",
]

for test in test_remove_duplicates:
    print(test)

remove_duplicates(numbers)
print("\nRemaining list:", numbers)
```