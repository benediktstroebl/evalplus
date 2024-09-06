```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 3))
```

The function `intersperse()` takes in a list of numbers `numbers` and an integer `delimiter` as parameters. If the input list is empty, it returns an empty list. Otherwise, it inserts the `delimiter` value after the first element of the list and then recursively calls itself to process the rest of the list. The final output is a list where every two consecutive elements of the original list are separated by the `delimiter`.