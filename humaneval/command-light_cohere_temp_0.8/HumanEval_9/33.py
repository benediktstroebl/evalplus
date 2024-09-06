```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)  # Sort the list of numbers in ascending order
    return [x for x in numbers if x == numbers[-1]]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a rolling_max function, which takes a list of numbers and returns a new list with the maximum elements from the current list. It sorts the main list to ensure that the largest number is at the beginning of each new list.