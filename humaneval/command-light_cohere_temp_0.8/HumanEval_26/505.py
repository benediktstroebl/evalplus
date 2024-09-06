```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert input list into a set, removing duplicates
    return list(numbers)  # Convert set back into a list

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 3, 1]
    result = remove_duplicates(numbers)
    print(result)  # Output: [1, 3, 4]
```
The code defines a function called `remove_duplicates` that takes a list of integers as an argument and returns a new list with all distinct integers from the original list. This is process converts the essential input into a set, which automatically eliminates duplicates. Then, it converts the set back into a list to provide the final, unique list of integers.