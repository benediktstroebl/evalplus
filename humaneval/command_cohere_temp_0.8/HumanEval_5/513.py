```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes a list of numbers `numbers` and an interspersing delimiter `delimiter` as input and returns a list of numbers with the delimiter inserted between each consecutive pair of elements in `numbers`. If `delimiter` appears in `numbers`, it is ignored. The delimiter is inserted enough times to guarantee that the final list has a length that is a multiple of `len(numbers)` to preserve its length.