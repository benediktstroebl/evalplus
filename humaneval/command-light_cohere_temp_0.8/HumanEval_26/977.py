```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))  # use set to remove duplicates and then convert back to list


numbers = [1, 2, 3, 2, 4, 3, 2, 5]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5]
``` 
This code uses the set data structure to remove duplicate values from a list of integers, then converts the set back to a list for the unique values. The code is self-contained and can be run as a standalone function, passing in a list of integers as an argument.