```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
```

The function takes in a list of numbers `numbers` and an interspersing delimiter `delimiter` and returns a new list where the delimiter is inserted between every two consecutive elements of the input list. If the input list is empty, it returns an empty list and if the delimiter is repeated in the input list, it still only returns it once in between two elements.