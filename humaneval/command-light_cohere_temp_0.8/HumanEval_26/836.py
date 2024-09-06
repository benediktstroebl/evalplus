```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove elements that occur more than once from a list of integers.
    """
    unique_counter = {}  
    return [num for num, _ in numbers.index(num, value=unique_counter.get(num) + 1)]
```
Here's a solution:
This function `remove_duplicates` takes a list of integers as an argument and returns a new list with all integers unique within the original list. The function uses a dictionary object to count the occurrences of each integer. It iterates through the unique element in numbers and updates the count in the dictionary.