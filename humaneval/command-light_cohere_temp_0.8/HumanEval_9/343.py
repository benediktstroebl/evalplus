```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)  # Sort the list of numbers in reverse
    return [x for x in numbers if x > numbers[-1]]  # list comprehension and generating rolling max
# this list is sorted in reverse order and contains numbers > current max
numbers[-1]

# Test case
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)

```