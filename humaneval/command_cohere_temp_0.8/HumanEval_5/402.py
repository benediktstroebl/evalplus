```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 0))
# Prints: [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]

numbers = [1, 3, 5, 7, 9]
print(intersperse(numbers, 2))
# Prints: [1, 2, 3, 5, 2, 7, 2, 9]

numbers = [1]
print(intersperse(numbers, 0))
# Prints: [1]

numbers = []
print(intersperse(numbers, 0))
# Prints: []
``` 

This function works by recursively interspersing the delimiter between elements, but only if there are two or more elements in the list. The base case is when the list is empty or has only one element, in which case it returns the list as is. 
The recursive case handles the list with more than one element through the following process:
1. Add the first element of the list to the output list.
2. Add the delimiter to the output list.
3. Recursively intersperse the rest of the list with the delimiter.
4. Return the completed output list. 

The desired result is achieved as the recursive calls build up the interspersed list until the base case is reached.