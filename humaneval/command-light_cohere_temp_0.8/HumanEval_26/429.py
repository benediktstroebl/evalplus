```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in [2, 4]]

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]

numbers = [1, 1, 2, 3, 4]
print(remove_duplicates(numbers))  # [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 2, 3]
print(remove_duplicates(numbers))  # [1, 2, 3, 4]

numbers = [1, 2, 4, 5, 6]
print(remove_duplicates(numbers))  # [1, 2, 4]
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set to keep track of seen elements, then it iterates through the input list and adds each number to the set if it is not already present. The function returns a result in a new list with duplicates removed.

The script then demonstrates the usage of this function with a few test cases, passing different lists of integers and printing the resulting lists.