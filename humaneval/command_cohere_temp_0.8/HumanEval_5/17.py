```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
```

The function takes in a list of numbers `numbers` and an int `delimiter` and returns a new list where the `delimiter` is inserted between every two consecutive elements of the input list `numbers`. The `result` list is initially constructed with all elements of `numbers` except the `delimiter`, and then extended with repeated occurrences of the `delimiter` to the length of the `numbers` list.