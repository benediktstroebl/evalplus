```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)  # Convert list to mutable Python list
    return [x for x in numbers if x > numbers[numbers.find_max()]][::-1]

# Unit tests
numbers_test = [1, 2, 3, 2, 3, 4, 3]
assert rolling_max(numbers_test) == [1, 2, 3, 3, 3, 4, 4], "Wrong rolling_max([1,2,3,2,3,4,3]) result"

numbers_capped = [1, 2, 3, 2, 3, 5]
assert rolling_max(numbers_capped) == [1, 2, 3, 3], "Wrong rolling_max([1,2,3,2,3,5]) result"

cap_with_one = [1, 2, 3]
assert rolling_max(cap_with_one) == [1, 2, 3], "Wrong rolling_max([1,2,3]) result"

```
This code defines a function called rolling_max that takes a list of integers as input and returns a new list with the largest elements from the original list after applying a rolling maximum definition to the original list. It uses the results and testing to ensure that the function is working correctly.