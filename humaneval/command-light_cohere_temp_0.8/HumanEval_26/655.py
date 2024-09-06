```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.is(seen)]


numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = ['apple', 'banana', 'apple', 'cherry']
result = remove_duplicates(numbers)
print(result)  # Output: ['apple', 'banana', 'cherry']

numbers = [1, 2, 3, 2]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3]
```

This solution defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set to keep track of elements seen before, then iterates through the input list and adds elements to the set if they are not duplicates and are not already in the output list.