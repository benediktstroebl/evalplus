```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.keys()]]

    for num in numbers:
        if num not in seen:
            seen.add(num)
    return numbers[:]
```
This code defines a function named `remove_duplicates` that takes a list of integers as an argument and returns a new list with all duplicate elements removed. The function utilizes a set data structure to keep track of elements that have already been seen, and then iterates through the input list, removing elements that are in the set or are in the keys of the input list.