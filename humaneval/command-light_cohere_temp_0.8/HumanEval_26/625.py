```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.keys()]]


numbers = [1, 2, 3, 2, 4, 2, 3, 1]
print(remove_duplicates(numbers))
``` 
The provided code defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a dictionary to store the duplicates and then uses a list comprehension to filter out the elements that are not in the keys list.