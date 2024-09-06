```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 1]

# Test cases
numbers_test = [1, 2, 3, 2, 4]
result_test = remove_duplicates(numbers_test)
print(result_test)  # Expected output: [1, 3, 4]

empty_list = []
result_empty = remove_duplicates(empty_list)
print(result_empty)  # Expected output: []

numbers_list = [5, 2, 8, 3, 6, 7]
result_list = remove_duplicates(numbers_list)
print(result_list)  # Expected output: [2, 3, 6, 7]
``` 
This Python script defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a unique set to keep track of encountered elements and then filters out any numbers that are less than one. The test cases demonstrate the expected behavior of the function.