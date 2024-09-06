```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test the function with a sample input
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)

# Test with empty list
numbers = []
result = remove_duplicates(numbers)
print(result)

# Test with list of strings
numbers = ['hello', 'world', 'hello', '!.']
result = remove_duplicates(numbers)
print(result)
``` 
This script defines a function `remove_duplicates` that removes duplicate elements from a list. The function takes a input of a list and returns a new list that contains only the unique elements from the original list. This is also passes tests to verify the correctness of the function. The script also provides test cases for different scenarios.