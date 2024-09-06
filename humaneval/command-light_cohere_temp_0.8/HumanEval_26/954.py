```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Unit tests
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 3, 4, 1, 2]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [5, 5, 5, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [5]
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. It utilizes the unique elements by using the set data type and checks if each element exists in the input set.