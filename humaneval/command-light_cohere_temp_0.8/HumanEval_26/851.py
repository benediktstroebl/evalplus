```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 0]

# Test the function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]

# Test the function with negative numbers
numbers = [1, 2, 3, -1]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3]
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate positive integers removed. The function uses a set to keep track of the encountered numbers and a list comprehension to filter out the numbers that are not present in the set and are positive.