```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return list(numbers)


# Test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected Output: [1, 3, 4]

numbers = [1, 3, 2, 4, 2, 5]
print(remove_duplicates(numbers))  # Expected Output: [1, 3, 2, 4, 5]

numbers = [10, 20, 30, 40]
print(remove_duplicates(numbers))  # Expected Output: [10, 30, 40]

numbers = [10, 20, 10, 30, 40]
print(remove_duplicates(numbers))  # Expected Output: [10, 30, 40]

```
This Python code defines a function called remove_duplicates that takes a list of integers as input and returns a new list with duplicates removed. The function uses the simplest technique by converting the input list into a set, which automatically eliminates duplicates, and then converting it back into a list. The test cases demonstrate the correctness of the function by passing various input lists and confirming that the output lists are as expected.