```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [result]
# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list that contains only unique elements. It uses a this set to keep track of numbers encountered before and then loops through the input list, appending only the numbers that aren not already in the set. This ensures that duplicates are removed and the result is a list of unique integers.