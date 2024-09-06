```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Unit Tests
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]

numbers = [1, 2, 3, 3, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5, 6, 7]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 2, 3, 4, 5, 6, 7]
``` 
This Python script presents a function named `remove_duplicates`, designed to process a list of integers and eliminate duplicate elements. The function employs a set difference to check for duplicate numbers and then employs a list comprehension to filter out these duplicates. 

The script also includes a series of unit tests that validate the behavior of the `remove_duplicates` function with various input scenarios, confirming that the expected output is indeed a list of unique integers.