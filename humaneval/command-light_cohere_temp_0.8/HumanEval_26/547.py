```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.count(seen)]


numbers = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(numbers)
print(result)

numbers = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(numbers)
print(result)

numbers = [4, 2, 4, 2]
result = remove_duplicates(numbers)
print(result)
```

This solution defines a function remove_duplicates that takes a list of integers as input and returns a new list with elements from the original list that do not appear more than once. The function uses a set to keep track of elements that have been encountered, and then returns a new list with elements that are not in the set and have not been seen before. The output of the list of integers is a list of distinct integers.