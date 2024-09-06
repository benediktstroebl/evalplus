```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
delimeter = 4

print(intersperse(numbers, delimeter))  # Expected output: [1, 4, 2, 4, 3]
``` 
Make sure you have the `typing` module imported in order to have the `List` type available as a annotation.

The function `intersperse()` takes a list of numbers `numbers` and an integer `delimeter` as input and returns a new list where each element of `numbers` is separated by `delimeter`. The base case of the recursive approach is when `numbers` is an empty list, in which case it returns an empty list. Otherwise, it concatenates the first element of `numbers` with a delimeter and the result of running `intersperse` on the rest of the list (`numbers[1:]`) recursively.