```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)


# Test cases
numbers1 = [1, 2, 3, 2]
numbers2 = [1, 2, 3, 4, 2]
numbers3 = [1, 1, 2, 3]
numbers4 = [1, 2, 3, 4, 5, 6]

print(remove_duplicates(numbers1))  # Output: [1, 2, 3]
print(remove_duplicates(numbers2))  # Output: [1, 2, 3, 4]
print(remove_duplicates(numbers3))  # Output: [1, 2, 3]
print(remove_duplicates(numbers4))  # Output: [1, 2, 3, 4]
```

This Python script presents a function called `remove_duplicates`, designed to process a list of integers and eliminate instances of duplicate elements. The function converts the process the list to a set, effectively removing any duplicates, and then returns a new list containing unique elements. The script provides several test cases to demonstrate the function's behavior.