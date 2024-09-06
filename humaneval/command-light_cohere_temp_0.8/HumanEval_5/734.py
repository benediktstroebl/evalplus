```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[::-1]

# Test the function
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 4)
print(result)  # Expected output: [1, 4, 2, 4, 3, 5]
``` 
The function `intersperse` is defined to take a list of numbers and a delimiter as input, and it returns a new list with the numbers separated by the delimiter. The function works by using a starting point for each new list element and adding the delimiter, then adding the element from the end of the list.