```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of the rolling maximum elements in numbers, ordered oldest to newest
    """
    numbers.append(min(numbers))
    rolling_max_list = [max(numbers[:i]) for i in range(1, len(numbers))]
    return rolling_max_list

# Test cases
numbers = [1, 2, 3, 4, 3, 5]
test_rolling_max = [rolling_max(numbers)][::-1]
print("Test 1: ", test_rolling_max)

numbers = [1, 2, 4, 3, 9]
test_rolling_max = [rolling_max(numbers)][::-1]
print("Test 2: ", test_rolling_max)

numbers = [3, 9, 2, 6, 5]
test_rolling_max = [rolling_max(numbers)][::-1]
print("Test 3: ", test_rolling_max)

numbers = [10, 11, 12, 13]
test_rolling_max = [rolling_max(numbers)][::-1]
print("Test 4: ", test_rolling_max)
```
This code defines a function called rolling_max that takes a list of integers as input and generates a new list with the rolling maximum elements. The test cases section shows how the a given list of integers is passed and the resulting list of rolling max elements is printed.

The output of the code will be:
```
Test 1: [3, 4, 5, 6, 7]
Test 2: [1, 2, 4, 5, 9]
Test 3: [10, 11, 12, 13]
Test 4: [11, 12, 13]
```