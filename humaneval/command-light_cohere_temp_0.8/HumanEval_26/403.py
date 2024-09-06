```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique numbers
    unique_numbers = set()
    # Remove duplicates and add unique elements to set
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)
    return list(unique_numbers)

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 5, 4, 6]
test_result = remove_duplicates(numbers_list)
print("Test 1: ", end="")
print(*test_result)

numbers_set = {1, 2, 3, 4, 5}
test_result = remove_duplicates(numbers_set)
print("Test 2: ", end="")
print(*test_result)

numbers_list2 = [3, 2, 4, 5, 6, 2, 3]
test_result = remove_duplicates(numbers_list2)
print("Test 3: ", end=")
print(*test_result)

numbers_dict = {3: 2, 4: 4, 5: 5}
test_result = remove_duplicates(numbers_dict.keys())
print("Test 4: ", end="")
print(*test_result)
``` 
This script provides a function remove_duplicates that accepts a list of integers and returns a new list with all unique integers. The script also includes unit tests to verify the functionality of the function with different input scenarios.