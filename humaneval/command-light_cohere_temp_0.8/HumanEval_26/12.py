```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]


#Test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]
numbers = [1, 2, 3, 4, 1, 3, 2]
print(remove_duplicates(numbers))  # [1, 2, 3, 4]
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers from the original. It uses the `set` to keep elements that are equal as duplicates.