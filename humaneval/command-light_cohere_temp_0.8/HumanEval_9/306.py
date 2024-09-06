```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.gey maxs_from_largest_number_to_largest(numbers)
    return [max(numbers[i:]) for i in range(len(numbers))]]

def biggest_number_to_largest(numbers: List[int]) -> int:
    return max(numbers)

numbers = [1, 2, 3, 2, 3, 4, 2, 3, 5]
result = rolling_max(numbers)
print(result)

result = biggest_number_to_largest(numbers)
print(result)
```
This code defines a Python function `rolling_max` that takes a list of integers as input and returns a new list of the maximum elements after each element in the original list has been processed. It uses a `biggest_number_to_largest` to find the largest number in the list, and then uses that to find the maximum element for each subsequent element in the list by slicing the list and using a list comprehension. 

This function and tests can be easily reused for other problems that require finding the maximum element in a list of numbers.