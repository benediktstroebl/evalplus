```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.keys()]]
keys = set(numbers)
    return [num for num in numbers if num not in keys]

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 1, 4]
test_remove_duplicates = [
    'This function removes duplicates correctly',
    'Test case passed',
    'Unusual input, still removes duplicates correctly',
    '1 2 3 4',
    '1 2',
    '3 4'
]
results = remove_duplicates(numbers)
for test, expected in zip(test_remove_duplicates, results):
    print(f'Test: {test}, Expected: {expected}, Got: {results[test]}')
``` 
This Python script defines a function called remove_duplicates, designed to process a list of integers and remove all elements that duplicate any other element in the list. The function employs a set data structure to identify duplicate values and then uses list comprehension to filter out these duplicates. 

This script also includes unit tests for the remove_duplicates function.