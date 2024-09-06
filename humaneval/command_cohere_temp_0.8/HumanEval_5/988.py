```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimeter = 3

expected_output = [1, 3, 2, 3, 4, 3, 5]
print( Intersperse(numbers, delimeter) )
```

The function `intersperse()` takes in a list of integers `numbers` and an int `delimeter` as input and returns a list of integers. This is achieved using a recursive approach by adding the `delimeter` to the list and then calling the function again on the rest of the list (`numbers[1:]`) until there is no list remaining, in which case we simply return the list with the first element only.