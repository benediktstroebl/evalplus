```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    return [set of distinct integers]
    numbers = [1, 2, 3, 2, 4, 3, 4]
    return [x for x in set(numbers) if x not in set(numbers)]

# Example
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
``` 
This function is self-contained and uses the set data structure to efficiently remove duplicate elements from the input list. It utilizes the