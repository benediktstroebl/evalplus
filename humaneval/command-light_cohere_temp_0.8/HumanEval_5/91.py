```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.

    : 'numbers': List[int],  delimiter: int ) -> List[int]:
    # Initialize empty list to store the result
    result = []

    # Iterate over each element in the input list
    for num in numbers:
        # If it's the first element, add the delimiter
        if len(result) == 0:
            result.append(num)
        # Otherwise, add the next element and the delimiter
        else:
            result.append(num)
            result.append(delimiter)

    # Return the final list of elements
    return result
```