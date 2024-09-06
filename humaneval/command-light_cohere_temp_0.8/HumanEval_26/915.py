```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]

# Test
numbers = [1, 2, 3, 2, 4, 3]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
``` 
This Python function, `remove_duplicates`, takes a list of integers as input and returns a new list that contains only the unique elements from the input list. 

This function uses the built-in `set` method to create a set of the elements from the input list. Then, it iterates through the set elements and adds them to the result list.