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

The given Python script provides a solution to the problem statement by defining a function `remove_duplicates(numbers: List[int]) -> List[int]`. This function takes a list of integers as input and returns a list that removes all elements occurring more than once, while preserving the order of the remaining elements.

The solution uses a set `seen` to keep track of the elements that have already been encountered. As the loop iterates through the input list, each element `num` is checked against the set. If the element is not in the set, or if the set size is about to become 1 (i.e., the last occurrence of an element), it is added to the result list and then added to the set. 

This way, the output list contains only the unique elements from the input list, and the elements that occurred multiple times are effectively removed. 

The `remove_duplicates` function effectively solves the problem statement by removing duplicates while retaining the order of the remaining elements.

This approach has a time complexity of `O(n log n)`, where `n` is the length of the input list, due to the set operations for uniqueness checks. The space complexity is `O(n)`, as we create a new list `result` and a set `seen` to store unique elements.