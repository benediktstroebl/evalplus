```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The algorithm is a typical set intersection problem: go through each number in order, and add it to the result list and the seen set, if it's not already in the seen set, or if the seen set only contains that number. This ensures that the result list only contains unique elements and maintains the order of numbers from the input list. 

To ensure the function handles the edge case where the input list might be empty or have no duplicates, you could add a test like this:
```python
assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
assert remove_duplicates([1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10]) == [1, 3, 5, 7, 10]
assert remove_duplicates([]) == []
``` 
If the given list is already unique, it should return the list as it is.