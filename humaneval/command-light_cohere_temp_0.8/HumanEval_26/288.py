```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in [x for x in numbers if x in seen]]


# Test suite
numbers = [1, 2, 3, 2, 4, 3, 2, 5]
print(remove_duplicates(numbers))
```
This code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The function uses a set to keep track of numbers that have been seen before, and then iterates through the input list, removing elements that have been seen before. The test suite uses a list of numbers and passes the function to the `remove_duplicates` function, which prints the resulting list.