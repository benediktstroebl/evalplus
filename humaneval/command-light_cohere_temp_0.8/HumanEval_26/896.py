Here is a self-contained Python script that solves the problem of removing duplicates from a list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return [num for num in numbers if num not in numbers]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 2, 5]

correct_output = [1, 3, 4]
assert remove_duplicates(numbers_list) == correct_output

```

The function `remove_duplicates` takes a list of integers and returns a new list with duplicates removed. The test code ensures that the function produces the correct output for the given input.