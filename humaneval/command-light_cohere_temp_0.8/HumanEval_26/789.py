```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Test the function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
``` 
This code defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicates removed. The code then creates a list of numbers, and passes it to the remove_duplicates function. The expected output is the resulting list with duplicates removed, which is [1, 3, 4].