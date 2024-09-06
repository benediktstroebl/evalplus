```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Test the function with a list of numbers
test_list = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(test_list)
print(result)  # Expected output: [1, 3, 4]

# Test the function with a list of strings
test_strings = ["this", "is", "duplicates", "test"]
result = remove_duplicates(test_strings)
print(result)  # Expected output: ["this", "is"]
``` 
This Python code defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The code then tests this function using both a list of numbers and a list of strings, and the expected output for both cases is the removal of duplicates.