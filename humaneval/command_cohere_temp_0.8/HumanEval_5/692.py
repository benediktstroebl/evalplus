```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an interspersing delimiter `delimiter` as inputs. It filters out the delimiter from the list and calculates the total number of delimiters required to intersperse among all the numbers. Lastly, it returns the interspersed list.