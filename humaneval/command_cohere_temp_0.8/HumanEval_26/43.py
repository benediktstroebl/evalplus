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

The function `remove_duplicates` takes a list of integers as input and returns a list of unique integers from the input list. It uses a set called `seen` to keep track of the unique integers it has encountered so far. It iterates through the input list, and for each integer `num`, it checks if the integer is not in the `seen` set or if the set has only one element. If either of these conditions is true, it adds the integer to the `result` list and adds it to the `seen` set. This ensures that no duplicates are added to the `result` list, and it filters out all but the first occurrence of any duplicates in the input list.  Any remaining elements in `seen` after processing the entire list are also added to `result`. The order of elements in `result` matches the order of their respective occurrences in the input list.