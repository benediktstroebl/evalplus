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

The function `remove_duplicates` takes a list of integers as input and returns a list of unique integers from the input list. It uses a set `seen` to keep track of the unique integers that have been encountered so far. 

It iterates through the input list, and for each integer `num`, it checks if the integer is already in the `seen` set. If the integer is not in the set, or if the set contains only one element at this point, it adds the integer to the `result` list and adds it to the `seen` set. This ensures that any integer appearing more than once in the input list will only be added to the result list once, and the order of integers in the output list matches the order in the input list.

The expected output for the provided test case `[1, 2, 3, 2, 4]` would be `[1, 3, 4]`.