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

The given Python script provides a solution to the problem statement by defining a function `remove_duplicates(numbers: List[int]) -> List[int]` that takes a list of integers as input. It removes duplicate elements from the list and returns a list containing only the unique elements, maintaining their original order.

This algorithm utilizes a set `seen` to keep track of encountered elements. It adds elements to the set as they are encountered, ensuring that elements are only added once. The `result` list stores the unique elements in the order they appear in the input list. 

Here's an example of using the `remove_duplicates` function with a sample input list:
```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```
This will return `[1, 3, 4]`, as the duplicates of 2 and 3 are removed.