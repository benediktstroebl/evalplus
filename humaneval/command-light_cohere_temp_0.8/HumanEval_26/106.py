```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.count()]]

numbers = [1, 2, 3, 2, 4, 3, 4, 5]
result = remove_duplicates(numbers)
print(result)
``` 
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list of integers with duplicates removed. The function uses a set to keep track of elements that have been encountered before, and then it iterates over the input list and adds elements to the set if they are not already in the set. After processing all elements elements, the function returns the new list with duplicates removed.