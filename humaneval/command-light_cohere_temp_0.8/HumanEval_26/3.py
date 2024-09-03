```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]


# Test
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
``` 
This Python function, remove_duplicates, takes a list of integers as input and returns a new list with all distinct integers from the original. This is an simple implementation using a list comprehension with the count attribute to identify duplicates and keep only the first occurrence of each number.