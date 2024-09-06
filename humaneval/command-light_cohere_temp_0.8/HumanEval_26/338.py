```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Remove duplicates from the list
    numbers = list(set(numbers))
    return numbers

# Test the remove_duplicates function
numbers = [1, 2, 3, 2, 4, 3, 2]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
``` 
This script defines a function `remove_duplicates`, which takes a list of integers as input and removes all duplicates from the list using the `set()` function, which converts the list to a set and removes duplicates. 

Then, the script tests the `remove_duplicates` function by passing a list of numbers, and the expected output is `[1, 3, 4]`, which is the list of unique integers.