```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.get(len(numbers),len())]]


# Test case 1
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print("Test case 1 result:", result)

# Test case 2
numbers = [5, 5, 5]
result = remove_duplicates(numbers)
print("Test case 2 result:", result)

# Test case 3
numbers = [1, 2, 3, 4, 5]
result = remove_duplicates(numbers)
print("Test case 3 result:", result)
``` 
This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers. The code then tests the can be modified to test with different input data.