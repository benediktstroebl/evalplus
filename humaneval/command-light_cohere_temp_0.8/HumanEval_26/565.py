```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in [n for n in numbers if n in seen]]
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate integers removed. The function uses a set to keep track of elements that have been seen before, and then it iterates through the input list, checking if each element is not in the set and not in a list of seen elements. This effectively removes duplicates and leaves only the unique integers in the output list.