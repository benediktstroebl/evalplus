```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.keyset()]]
uniq_numbers = []
    for num in numbers:
        if num not in seen and num not in numbers[numberset()]:
            seen.add(num)
            uniquestable.append(num)
    return uniquestable
```

This code implements a function `remove_duplicates` that takes a list of integers as input and returns a new list with all unique integers from the input list. The function utilizes a set data structure to keep track of the integers that have been seen, and then it iterates through the input list, appending integers to the `seen` set if they are not duplicates of any other elements in the input list. This ensures that the unique integers are retained in the output list.