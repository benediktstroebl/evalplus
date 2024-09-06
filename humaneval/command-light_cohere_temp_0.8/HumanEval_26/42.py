```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]
This function, `remove_duplicates`, takes a list of integers as input and returns a new list with all unique integers. It uses the this List[int] `count()` method to get the number of occurrences of each element in the list. It then uses a list comprehension to filter out all elements that have already occurred in the list at least once.