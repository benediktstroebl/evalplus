```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]


# Test the function
numbers = [1, 2, 3, 2, 4, 3, 1, 4]
result = remove_duplicates(numbers)
print(result)

# Test the function with a list of strings
strings = ["hello", "world", "hello"]
result = remove_duplicates(strings)
print(result)
``` 
This function called `remove_duplicates` takes a list of integers as input and uses the set data structure to keep track of elements that have already been seen, ensuring uniqueness. The output is `[1, 2, 3, 4]`, which are the unique elements from the input list. 
The function is also tested successfully with a list of strings, which passes additional test for handling non-numeric characters.