```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.keys()]]


numbers = [1, 2, 3, 2, 4, 3, 1, 4]
print(remove_duplicates(numbers))

numbers = ['apple', 'carrot', 'pomegranate', 'elderberry']
print(remove_duplicates(numbers))

numbers = [1, 1, 2, 3]
print(remove_duplicates(numbers))

numbers = [1, 2, 1, 2]
print(remove_duplicates(numbers))

numbers = [1, 1, 1]
print(remove_duplicates(numbers))
```

This Python code defines a function called `remove_duplicates`, which takes a list of integers as input and returns a new list that removes duplicate occurrences. The code demonstrates the example usage by passing a list of numbers and then a list of strings, and it prints the results of each call to the `remove_duplicates` function.