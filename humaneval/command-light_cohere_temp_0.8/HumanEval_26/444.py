```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num > 0]

# Test cases
numbers1 = [1, 2, 3, 2]
numbers2 = [4, 2, 2, 3, 1]
numbers3 = [5, 6, 7, 8, 9]
numbers4 = [None, None, None]

# Call the remove_duplicates function with different inputs and assertions
result1 = remove_duplicates(numbers1)
assert len(result1) == 3

result2 = remove_duplicates(numbers2)
assert len(result2) == 1

result3 = remove_duplicates(numbers3)
assert len(result3) == 4

result4 = remove_duplicates(numbers4)
assert len(result4) == 0
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique positive integers. The function uses a set to keep track of the unique elements and returns the list of elements that are not present in the set and are greater than 0. The script also includes several test cases to validate the correctness of the `remove_duplicates` function.