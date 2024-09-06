```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This Python script defines a function called `remove_duplicates` that takes a list of integers as input. It removes any elements that occur more than once from the input list and returns a unique list of integers in the same order as the input list. 

The `remove_duplicates` function utilizes a set called `seen` to keep track of unique elements encountered while iterating through the input list. It adds only the first occurrence of each element to the `result` list, which stores the unique elements. 

The function returns the `result` list containing all the unique elements in the same order as they appeared in the original input list, ensuring that the script retains the original order of elements while removing duplicates. 

This solution is both efficient and well-documented, providing a clear understanding of the problem and its solution.