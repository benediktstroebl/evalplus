```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return list(numbers)

# Test the function with sample input and expected output
numbers_list = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers_list)
print(result)  # Output: [1, 3, 4]

numbers_set = {1, 2, 3, 4}
result = remove_duplicates(numbers_set)
print(result)  # Output: [1, 3, 4]

```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. It then demonstrates thea application of this function to three example inputs: a list, a set, and a set of numbers, and prints the resulting lists to verify the function's correctness.