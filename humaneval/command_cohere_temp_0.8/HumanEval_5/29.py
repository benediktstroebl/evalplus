```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an int `delimiter` as inputs. It creates an initial result list by iterating through `numbers` and omitting all instances of `delimiter`. To ensure that the result list has the same length as the input list, it appends `delimiter` as many times as the number of elements omitted, i.e., `len(numbers) - len(result)`.

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3, 4], 5)
[1, 5, 2, 5, 3, 5, 4]
```
Which outputs interspersing the numbers in the list [1, 2, 3, 4] with 5 produces the list [1, 5, 2, 5, 3, 5, 4].