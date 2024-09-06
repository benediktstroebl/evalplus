```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in sorted(numbers) if x > numbers[-1]]

# Test case 1: Single number list
single_number_list = [5]
result = rolling_max(single_number_list)
assert len(result) == 1
assert result[0] == 5 

# Test case 2: List with duplicate elements
numbers = [1, 2, 2, 3, 3]
result = rolling_max(numbers)
assert len(result) == 4
assert result == [1, 2, 2, 3] 

# Test case 3: List with random order
numbers = [4, 5, 6, 7]
result = rolling_max(numbers)
assert len(result) == 3
assert result == [5, 6, 7] 

# Test case 4: Provide empty list
numbers = []
result = rolling_max(numbers)
assert len(result) == 0
```
This Python script defines a function called `rolling_max` that takes a list of integers as input and returns a new list containing the elements from the original list that are greater than the last element in the sequence. 

The `rolling_max` function uses a list comprehension to generate this new list. 
It uses the `sorted` function to sort the elements in ascending order, and then it uses a list comprehension to select the elements that are greater than the last element in the sorted sequence.

This script provides several test cases to verify the correctness of the `rolling_max` function.