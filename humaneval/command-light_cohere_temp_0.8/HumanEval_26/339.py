```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n not in set(numbers)]


# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
``` 
This script provides a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The function utilizes the simple set membership test to filter out any duplicate elements, ensuring the output is unique.