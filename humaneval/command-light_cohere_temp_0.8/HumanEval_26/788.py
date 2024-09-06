```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]


# Test cases
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]

numbers = [1, 2, 3, 2, 4, 2]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]

numbers = [1, 2, 3, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]

numbers = [1, 2, 3, 4, 2, 6]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 2, 3, 4]
```
This script defines a function called `remove_duplicates`, which takes a list of integers as an argument and returns a new list with any duplicate elements removed. The test cases pass the use this function on a variety of input lists and print the results to verify the expected output.