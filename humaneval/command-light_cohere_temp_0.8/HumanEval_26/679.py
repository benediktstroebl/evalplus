```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.count() > 1]]


# Test
numbers = [1, 2, 3, 2, 4, 3, 1]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
``` 
This function removes duplicate elements from a list of integers and returns a new list with unique elements.  It takes the using a set data structure to keep track of the elements we have already seen, it iterates through the input list, and for each element, it checks if the element is not in the seen set. If the element is not in the seen set and not in the original list, it is added to the output list.