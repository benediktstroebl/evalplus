```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.keyset()]
    more than once]

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)

numbers = [1, 2, 3, 2, 4, 2]
result = remove_duplicates(numbers)
print(result)

numbers = [1, 2, 3, 4, 5, 6]
result = remove_duplicates(numbers)
print(result)
```
This Python code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. 

The function uses a `set` data structure to keep track of seen elements and then iterates through the input list, removing elements that are present in both the input list and the `seen` set. 

The code then demonstrates the function with several test cases, printing the input list and the resulting list with duplicates removed.