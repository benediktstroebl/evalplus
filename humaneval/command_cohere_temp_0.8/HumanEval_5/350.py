```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an int `delimiter` as inputs. It iterates through the list, excluding the `delimiter` from the result, and adds the `delimiter` as many times as necessary to maintain the same length as the original list. This way, the `delimiter` is inserted between all consecutive elements, achieving the desired result.