```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.keys()]]


# Test
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
``` 
This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The function achieves this using a key idea of iterating through the input list twice: once element is encountered for the first time, it is added to a set that keeps track of unique elements. Then, the second iteration is used to filter out these duplicate elements.