```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]

# Test cases
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # expected output: [1, 3, 4]
numbers = [1, 2, 3, 2, 4, 2, 3]
result = remove_duplicates(numbers)
print(result)  # expected output: [1, 2, 3]
numbers = [1, 2, 3, 4, 5, 6]
result = remove_duplicates(numbers)
print(result)  # expected output: [1, 2, 3, 4]
``` 
This script provides a function `remove_duplicates` that accepts a list of integers and outputs a list of unique integers. It uses the unique element strategy to filter duplicates, which involves checking each element against every other element in the input list.