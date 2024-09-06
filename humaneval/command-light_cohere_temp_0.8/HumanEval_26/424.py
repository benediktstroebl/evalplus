```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in set(numbers) if n not in numbers]

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)

numbers = [1, 1, 2, 3, 3, 4]
result = remove_duplicates(numbers)
print(result)

numbers = [1, ,3, 4]
result = remove_duplicates(numbers)
print(result)

numbers = [4, 1, 2, 2, 3, 3]
result = remove_duplicates(numbers)
print(result)
```
This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with elements that are not present in the input list more than once. The function uses the particular approach. It then tests tests a tested using several sample inputs, which include lists with duplicate elements, and lists with no duplicates. The expected output is the list with elements 1, 2, 3, and 4, regardless of the input format.