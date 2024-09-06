Here's the improved and self-contained solution:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```
This code defines a function `remove_duplicates` which takes a list of integers as input and returns a new list that contains unique integers from the original list. The function uses a set `seen` to keep track of numbers that have already been encountered, and it iterates through the input list. Then, for each number in the list, it checks if the number is already in the set, if it's not, then it adds the number to the set and appends it to the result list.

This is a self-contained solution, and the function can be used as a stand-alone method to remove duplicates from any list of integers. The function's output is tested using the test code provided earlier.