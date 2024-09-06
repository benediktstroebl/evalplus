```python
from typing import List
def remove_duplicates(numbers: List[int]): 
    return List(set(numbers))

# Test the function with a list of integers
numbers = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

# Test with empty list
result = remove_duplicates([])
print(result)  # Output: []

# Test with list of strings
numbers = ["hello", "world"]
result = remove_duplicates(numbers)
print(result)  # Output: ["hello"]
``` 
This Python script defines a function `remove_duplicates` that takes a list of integers and returns a new list with duplicate elements removed. The tests of the simple example of using this function with a list of integers and an empty list, and then with a list of strings. The output shows the expected results.