```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes a list of numbers `numbers` and an int `delimiter` as input and returns a list where each number is either preceded or followed by the `delimiter`, or both, so as to ensure that the `delimiter` repeats as often as possible. An empty list and a list with only one element (the `delimiter`) returns an empty list.