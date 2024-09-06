```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize a set to store unique numbers
    unique_nums = set(numbers)
    return [num for num in unique_nums if num not in numbers]

# Test the remove_duplicates function
numbers_to_test = [1, 2, 3, 2, 4, 3, 5, 4]
result = remove_duplicates(numbers_to_test)
print(result)  # Expected output: [1, 3, 4]
``` 
This code implements a function **`remove_duplicates`** that takes a list of integers as input and returns a new list that contains only the unique integers from the input. The function uses the unique set to keep track of the unique integers.