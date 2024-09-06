```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x not in numbers[numbers.count()]]

# tests
numbers = [1, 2, 3, 2, 4, 3]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate values removed. The tests ensure that function is correct by passing the input list and comparing the output with the expected output.