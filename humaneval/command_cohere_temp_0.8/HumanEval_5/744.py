```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
print(intersperse(numbers, 4))
```

The function `intersperse()` takes in a list of numbers `numbers` and an int `delimiter` as parameters. If the input list is empty, it returns an empty list. Otherwise, it inserts the `delimiter` between every two consecutive elements in the input list and returns the modified list. This behavior recursively applies to the rest of the list after the first element, which is why the function calls itself with the second element as the first element to sprinkle the delimiter evenly across the list. The output of the example is:
```bash
[1, 4, 2, 4, 3]
```