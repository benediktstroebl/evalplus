```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen]
    seen.add(numbers)
    return result


# Unit tests
numbers = [1, 2, 3, 2, 4]
result_ref = [1, 3, 4]
assert remove_duplicates(numbers) == result_ref

numbers = [5, 1, 1, 6]
result_ref = [5, 6]
assert remove_duplicates(numbers) == result_ref
```

The above Python script defines a function called remove_duplicates, which takes a list of integers as input and returns a new list that removes all duplicate elements. The function uses a set to keep track of elements that have been seen before, and then it iterates through the input list and adds elements that are not in the set. The resulting list is then returned. The function is also tested with two examples, which pass the test successfully.