Here is a self-contained Python script that solves the problem of removing duplicates from an input list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult

# Example usage:
numbers = [1, 2, 3, 2, 4, 1]
print(remove_duplicates(numbers))
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set to keep track of elements that have been seen before, and then iterates through the input list, adding elements to the result list if they are not in the seen set.

This function can be used to efficiently remove duplicates from any list of integers, making it a reusable and self-contained solution for the given problem.