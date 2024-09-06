```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen]
    seen.add(numbers)
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```
This Python function, remove_duplicates, takes a list of integers as input and returns a new list with all integers not previously seen in the input list. The seen set keeps track of elements encountered, and the function filters out duplicate elements from the input list, ensuring that the output list does not contain duplicates.