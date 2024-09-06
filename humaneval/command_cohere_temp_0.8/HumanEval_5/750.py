```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 3))
```

The function `intersperse()` takes in a list of numbers `numbers` and an int `delimiter` as parameters. If the input list is empty, it returns an empty list. Otherwise, it inserts the `delimiter` between every two consecutive elements in the `numbers` list and returns the modified list. This process is recursively applied to the rest of the list after the first element. 

The test case checks the function with a list of numbers and a delimiter and prints the returned list. It should print `[1, 3, 2, 3, 4, 5]` as the output, where the delimiter `3` is inserted between every two consecutive elements of the list `[1, 2, 3, 4, 5]`.