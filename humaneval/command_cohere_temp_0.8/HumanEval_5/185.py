```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes a list of numbers `numbers` and an int `delimiter` as input and returns a list where every two consecutive elements are separated by `delimiter`. If `delimiter` occurs in the input list, it will be added to the output list only when there is a gap between two consecutive elements that is at least as large as `delimiter`. This ensures that `delimiter` is added in such a way that the list remains contiguous.