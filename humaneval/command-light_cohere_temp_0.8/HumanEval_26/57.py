```python
from typing import List
def remove_duplicates(numbers: List[int]): 
    return List(set(numbers))

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result) # Output: [1, 3, 4]
``` 
The function `remove_duplicates` takes a list of integers and returns a new list that contains only the distinct elements. This is using the the unique elements in the input list, and removes all duplicates.