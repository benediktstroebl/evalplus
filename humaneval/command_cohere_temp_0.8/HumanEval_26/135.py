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

The given Python script provides a solution to the problem statement by defining a function `remove_duplicates(numbers: List[int]) -> List[int]` that takes a list of integers as input and returns a list of unique integers from the input list. It uses a set called `seen` to keep track of the unique integers encountered while iterating through the input list. It adds integers to the set as they are encountered, and if an integer is encountered for the second time, it is not added to the `seen` set, and hence not added to the `result` list. The final list `result` contains only the unique integers from the input list, preserving their original order. 

The solution is self-contained and does not rely on any external modules or assumptions beyond those implied by the type annotation.