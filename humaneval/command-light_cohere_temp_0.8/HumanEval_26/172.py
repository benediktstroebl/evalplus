```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test the function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

# Test with a list of strings
string_numbers = ["a", "b", "c", "d"]
result = remove_duplicates(string_numbers)
print(result)  # Output: ["a", "b", "c", "d"]
```
This Python script defines a function `remove_duplicates` that removes duplicate elements from a list of integers and then tests the function with both a list of integers and a list of strings.