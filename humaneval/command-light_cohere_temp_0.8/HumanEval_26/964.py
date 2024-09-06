```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x not in numbers[numbers.count(numbers)]
```
This Python function, `remove_duplicates`, takes a list of integers as an argument. It returns a unique elements from the list, which are numbers that are not present more than once in the input list. The function uses a type hint `List[int]` to pass in the list of integers, and a list comprehension is used to filter out the duplicates.

The function utilizes the `count(numbers)` to find the number of occurrences of each element in the list, and then uses the list comprehension to only include elements that are not in the list of `numbers` more than once. 
This approach ensures that all duplicates are removed from the list while keeping the order of elements intact.