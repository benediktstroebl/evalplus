```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimeter = 4

expected_result = [1, 4, 2, 4, 3, 4, 5]

assert intersperse(numbers, delimeter) == expected_result
``` 

The function `intersperse()` takes in a list of numbers and a delimeter as input and returns a list of numbers with the delimeter inserted between each consecutive pair of numbers. The delimeter is also inserted between the first number and an empty list, and between the last number and the rest of the list.