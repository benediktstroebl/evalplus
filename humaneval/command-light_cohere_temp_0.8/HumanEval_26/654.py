```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes duplicate elements from the list.
    : Returns a full list without duplicates.
    """

    list comprehension is a good approach to this problem.

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
numbers2 = [2, 2, 4, 2]
result2 = remove_duplicates(numbers2)
print(result2)  # Output: [2, 4]
``` 
This script defines a function **remove_duplicates** that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses list comprehension to achieve this.