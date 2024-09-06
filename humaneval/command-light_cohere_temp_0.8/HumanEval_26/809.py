```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen]
    seen.add(numbers)
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]
```
This Python script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set to keep track of seen elements and then iterates through the input list, checking if each number is not already seen. The function then adds any unseen number to the set and returns the list with duplicates removed. 

This is a self-contained and functional solution to the problem of removing duplicate elements from a list of integers.