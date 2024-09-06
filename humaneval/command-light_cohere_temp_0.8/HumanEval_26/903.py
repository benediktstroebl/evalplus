```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.ices()]]


numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```
This script defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set to keep track of elements that have been seen before, and then it iterates through the input list and adds elements to the set if they are not in the original list or not already seen before. The output of the function is a list of integers with no duplicates.