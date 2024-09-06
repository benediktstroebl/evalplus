```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return list(set(numbers))

# Test the function with a sample input
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]

# Test with another sample input that contains duplicates
numbers = [1, 2, 3, 4, 2]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]
```
This Python function called `remove_duplicates` takes a list of integers as input and returns a new list that contains only the unique elements from the original list. It utilizes the strategy of removing duplicates by converting the input list into a set and then back into a list.