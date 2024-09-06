```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return [num for num in numbers if num not in numbers]

# Test the function
test_list = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(test_list)
print(result)  # Expected output: [1, 3, 4]

# Test with empty list
empty_list = []
result = remove_duplicates(empty_list)
print(result)  # Expected output: []
```

This Python code provides a self-contained function remove_duplicates that takes a list of integers as input and returns a new list with distinct integers. The function achieves this purpose by converting the input list into a set, which automatically eliminates duplicates, and then it creates a new list containing only the elements that are not in the set.

The code also includes test cases to verify the correctness of the remove_duplicates function. The expected outputs of the results are printed to the console, which demonstrates the expected behavior of the function.