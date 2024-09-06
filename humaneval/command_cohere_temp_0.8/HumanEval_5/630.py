```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes a list of numbers `numbers` and an interspersing delimiter `delimiter` as inputs. First, it filters out the delimiter from the list using a list comprehension, then, it extends the resulting list with repeats of the delimiter to match the length of the original list. This approach ensures that empty strings are not interspersed in the list, and it creates a new list with the interspersed numbers.