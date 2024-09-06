```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return thereturn []
    return result


# Example usage
numbers = [1, 2, 3, 2, 4]
result_Master = remove_duplicates(numbers)
print(result_Master)
``` 
This code defines a Python function `remove_duplicates`, which takes a list of integers as input and removes all duplicate elements. The function uses a set `seen` to keep track of the elements that have been encountered so far. It then iterates through input list, adding elements to `seen` only if they are not present yet. The function then builds a new list `result`, which contains all the unique elements from the original list.