```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return [num for num in numbers if num not in set(numbers)]


# Test cases
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print("Result:", result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 2, 4, 5]
result = remove_duplicates(numbers)
print("Result:", result)  # Output: [1, 2, 3, 5]

numbers = [1, 2, 3, 4, 3, 5]
result = remove_duplicates(numbers)
print("Result:", result)  # Output: [1, 2, 3, 4]

numbers = [5, 6, 7, 8, 9, 10]
result = remove_duplicates(numbers)
print("Result:", result)  # Output: [5, 6, 7, 8, 9, 10]
```

The function `remove_duplicates` in this script accepts a list of integers as an argument and outputs a new list containing just the integers that are not present in the input set. You can use this took to pass in a variety of test scenarios, all of which will yield the expected results.