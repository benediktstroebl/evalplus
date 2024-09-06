Here is a Python script that contains a self-contained function to solve the problem of removing duplicates from a list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    duplicates = set(numbers)
    return [num for num in numbers if num not in duplicates]

# Test the function
numbers = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 3, 5, 6]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5, 6, 7]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5, 6]
```

The function `remove_duplicates` takes a list of integers as input and returns a new list that contains only the unique elements from the input. The set method is used to convert the input list into a set, which removes duplicates automatically.

The test cases demonstrate the expected outputs, as each element is unique and does not appear more than once in the output list.