```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[0]]

# Test the function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)

# Test with list of strings
numbers_str = ['1', '2', '3', '2']
result_str = remove_duplicates(numbers_str)
print(result_str)
``` 
This script defines a function `remove_duplicates` that takes a list of integers and returns a new list with duplicate integers removed. The function uses a set to keep track of seen integers, and the function iterates through the input list, checking each element against the seen set and the first element of the list. The output will be a list with integers 1, 3, and 4, and in the case of passing a list of strings, the output will be the list with strings '1', '2', '3', '2'.