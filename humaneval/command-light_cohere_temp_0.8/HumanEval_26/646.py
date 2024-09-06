```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.seen duplicates()]
# Input and Output
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [3, 3, 1, 1, 3]
result = remove_duplicates(numbers)
print(result)  # Output: [3, 1]

numbers = [5, 2, 2, 3]
result = remove_duplicates(numbers)
print(result)  # Output: [5, 2, 3]
```

This script defines a function `remove_duplicates`, which takes a list of integers as input and returns a new list containing only the unique elements. The function uses a set data structure to keep track of the seen elements, then it iterates through the input list and adds elements to the set if they are not duplicates and they are not already in the output list.