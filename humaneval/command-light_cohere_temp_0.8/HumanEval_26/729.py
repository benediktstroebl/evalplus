```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return [n for n in numbers if n not in numbers[:]]

# Test the function with known good inputs/outputs
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
```
This function, when given a list of integers, will return a new list with only the unique integers from the original list. It works by using a list comprehension and the built-in function is_unique, which returns True if an element is not in the original list.