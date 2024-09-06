```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
print(intersperse(numbers, 4))
```

The function takes in a list of numbers and an integer delimiter as input and returns a list of numbers with the delimiter inserted between each consecutive pair of numbers. The base case of the recursion returns just the delimiter if the input list is empty, and the recursive case intersperse's the delimiter through the rest of the list.