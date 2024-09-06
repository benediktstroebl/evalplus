```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test the remove_duplicates function with a sample input
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)

# Test the function with list of different data types
mixed_data = [4, 2, 'string', 1]
result_mixed = remove_duplicates(mixed_data)
print(result_mixed)

# Test the function with a list of lists
nested_data = [[1, 2], [3, 4], [5, 6]]
result_nested = remove_duplicates(nested_data)
print(result_nested)
``` 
This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The `remove_duplicates` function uses the `set()` function to create a set from the input list, which automatically removes duplicate elements. 

Finally, the code provides several tests for the `remove_duplicates` function by passing different types of lists as input, and it prints the resulting lists to ensure the function is working correctly.