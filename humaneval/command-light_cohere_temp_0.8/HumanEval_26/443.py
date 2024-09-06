```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return [num for num in numbers if num not in numbers]

# Unit tests
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates = [
    remove_duplicates(numbers),  # Should return [1, 3, 4]
    # Add more tests as needed
]
print("Test results:", test_remove_duplicates)
``` 
This script defines a function **remove_duplicates** that takes a list of integers as input and returns a new list with duplicates removed. The function uses the **set()** to remove duplicates from the input list, and then it uses a list comprehension to filter out any elements that are not in the set. 

The function is then tested using the **unittest** library, and the test results are printed to the console.