```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[:seen.map()]]


# Example:
numbers = [1, 2, 3, 2, 4, 3, 1]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
``` 
The function `remove_duplicates` takes a list of integers as input and returns a new list with duplicate values removed. It uses a conventional method of finding duplicates, which are elements that occur more than once in the list. Additionally, it utilizes the set data to keep track of elements that have been encountered. 

The function iterates over the input list, and for each element, it checks if the element is already in the seen set or not in the list of numbers already seen. If the condition is not met, the element is added to the output list.