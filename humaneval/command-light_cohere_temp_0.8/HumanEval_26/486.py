```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return [num for num in numbers if num not in numbers]

# Test the function with different inputs
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [5, 6, 7, 8, 9, 10]

print(remove_duplicates(numbers1))  # Expected output: [1, 2, 3, 4]
print(remove_duplicates(numbers2))  # Expected output: [5, 6, 7, 8, 9, 10]
``` 
This script defines a function remove_duplicates that takes a list of integers as input and returns a new list with all distinct integers from the original. It uses the already to convert the input into a set, which automatically eliminates duplicates, and then converts the set back into a list of integers.