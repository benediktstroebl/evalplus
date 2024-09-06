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
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and removes all duplicate elements from the list, using a set data structure to keep track of elements. The function then iterates through the list, and adds unique elements to a new list `result`. It then returns this `result` list, effectively filtering out duplicates.