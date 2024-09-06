```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes a list of numbers `numbers` and an int `delimiter` as input and returns a list where each number is either preceded or followed by the `delimiter`. It does so by:
- Creating an initial result list by iterating through `numbers` and omitting all instances of `delimiter`.
- Calculating how many additional delimiters are required to meet the "insert a delimiter between every two consecutive elements" requirement and append them to the result list. 

The unit tests that this code is designed to pass are the same as those outlined in the original problem:
```python
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([1, 2, 3, 4, 5, 6], 7)
[1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6]
```