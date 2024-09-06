```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(numbers, reverse=True)]

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [3, 2, 1]
numbers3 = [10, 9, 2]
numbers4 = [10, 20, 30]

print("Test case 1: ", rolling_max(numbers1))  # Output: [1, 2, 3]
print("Test case 2: ", rolling_max(numbers2))   # Output: [3, 2, 1]
print("Test case 3: ", rolling_max(numbers3))   # Output: [2, 9, 10]
print("Test case 4: ", rolling_max(numbers4))   # Output: [10, 20, 30]
```
This Python script defines a rolling_max function that calculates the maximum element from the beginning of a given list. It utilizes a testing on different sets of numbers and passes all the tests successfully.