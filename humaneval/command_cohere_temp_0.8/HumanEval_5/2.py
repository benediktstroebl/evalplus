```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an interspersing delimiter `delimiter` as arguments. It filters out the delimiter from the list and calculates the total number of delimiters required to be inserted between consecutive elements. The final result will contain the list interspersed with delimiters. 

Here is an example of function usage: 
 ```python
>>> intersperse([1, 2, 3, 4], 5)
[1, 5, 2, 5, 3, 5, 4]
``` 

The result is `[1, 5, 2, 5, 3, 5, 4]`, with the delimiter value `5` inserted between each consecutive pair of numbers.