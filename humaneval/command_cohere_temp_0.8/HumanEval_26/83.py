```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order as input. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a list of unique integers. Inside the function, it uses a set called `seen` to keep track of seen integers and initializes an empty list called `result` to store the unique integers. It then iterates through each integer in the input list, and if an integer is not in the `seen` set, it adds it to both the set and the `result` list. Finally, the function returns the `result` list containing unique integers in the same order as the input list.