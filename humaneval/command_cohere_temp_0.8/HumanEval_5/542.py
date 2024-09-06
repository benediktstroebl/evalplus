```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
delimeter = 4

print(intersperse(numbers, delimeter))  # Expected output: [1, 4, 2, 4, 3]
``` 
The function `intersperse()` takes in a list of numbers `numbers` and an int `delimiter` as arguments. If the input `numbers` is empty, it returns an empty list. Otherwise, it inserts the `delimiter` between every two consecutive elements in the `numbers` list and returns the modified list. This process is recursively applied to the rest of the list after the first element.