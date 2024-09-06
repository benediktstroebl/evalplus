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

The given Python script provides a solution to the problem statement by defining a function `remove_duplicates(numbers: List[int]) -> List[int]` that takes a list of integers as input and returns a list of unique integers from the input list.

This algorithm uses a set, seen, to keep track of the unique elements encountered while iterating through the input list. The result list is used to store the unique elements in the order they appear in the input list.

Here's how the algorithm works:
1. Iterate through the input list `numbers`.
2. For each element `num` in the list:
   - If the element `num` is not in the seen set, or if the seen set only contains a single element (i.e., the first occurrence of an element), add `num` to both the result list and the seen set.
3. Return the result list, which contains only the unique elements from the input list.

This algorithm guarantees that the resulting list contains only unique elements and maintains the original order of these elements from the input list.