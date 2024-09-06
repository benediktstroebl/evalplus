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
This function takes a list of integers as input and creates a set to keep track of the unique numbers encountered. It then iterates through list, and for each number, it checks if the number is already in the set. If it's not, it adds the number to both the set and the result list.

The function returns a new list containing only the numbers that were not duplicate. This approach ensures that duplicate numbers are effectively removed from the list.