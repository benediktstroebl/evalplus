```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an int `delimiter` as inputs. It constructs a new list `result` where it either retains int values from `numbers` if they are not equal to `delimiter` or adds a delimiter int to the `result` list. The final step is to add delimiters to fill the remaining space, where the number of delimiters is calculated by `(len(numbers) - len(result))`. This allows the function to achieve the desired result of inserting `delimiter` between all consecutive elements of `numbers`.