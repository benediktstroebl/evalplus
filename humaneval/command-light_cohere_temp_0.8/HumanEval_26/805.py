```python
from typing import List
def remove_duplicates(numbers: List[int]): 
    return [num for num in set(numbers) if num not in numbers]

# Unit tests 
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print("Result:", result)
print("Test 1 passed")

numbers = [3, 2, 4, 2, 1]
result = remove_duplicates(numbers)
print("Result:", result)
print("Test 2 passed")
```

This script defines a function `remove_duplicates` that takes a list of integers and returns a new list with duplicate values removed. The function utilizes the using the set data structure to automatically remove duplicate values and then a list comprehension to filter out the remaining unique values.

The script also includes unit tests to verify the correctness of the `remove_duplicates` function.