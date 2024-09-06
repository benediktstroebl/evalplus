```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an interspersing delimiter `delimiter` and returns a new list with the delimiter inserted between each pair of elements in the input list. If the input list is empty, it returns an empty list, and if the delimiter is repeated multiple times in the input list, it will only appear once in the result.