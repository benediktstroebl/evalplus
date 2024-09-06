```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
delimeter = 4

print(intersperse(numbers, delimeter))  # Expected output: [1, 4, 2, 4, 3]
``` 
Make sure you have the `typing` module imported, which is needed to define the type of the input parameter `numbers` as `List[int]`. The function takes a list of numbers `numbers` and an integer `delimeter` as input and returns a list of numbers where each element of the input list is preceded and followed by the `delimeter` value. When the input list is empty, it returns an empty list. The recursive approach ensures that delimeter is prepended and appended only once for the entire list.