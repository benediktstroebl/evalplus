```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an int `delimiter` as inputs. It iterates through the list, excluding the `delimiter` from the result, and adds the `delimiter` to the result countlessly to ensure the same number of `delimiters` as there are elements in the list. It returns the list of numbers with the delimiter inserted between each consecutive pair of elements.