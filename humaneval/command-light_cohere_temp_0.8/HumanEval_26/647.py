```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return the
    result
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
result_map = remove_duplicates(numbers)
print(result_map)  # Expected output: [1, 3, 4]
``` 
This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list that removes all duplicates from the input list. The function uses a set to keep track of seen numbers and creates a new list with elements that were not in the seen set. The example usage demonstrates how the expected output would be `[1, 3, 4]`.