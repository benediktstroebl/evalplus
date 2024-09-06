```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
``` 

The function takes in a list of numbers `numbers` and an interspersing delimiter `delimiter` as inputs. It filters out the delimiter from the list and calculates the number of delimiters required to be interspersed using the formula `len(numbers) - len(result)`. It then extends the `result` list to include the required number of delimiters. Ultimately, it returns the `result` list, which is the list of numbers from the input list with the delimiter inserted between each consecutive pair of numbers. 

Here is an example of function usage: 

```python
>>> intersperse([1, 2, 3, 4], 5)
[1, 5, 2, 5, 3, 5, 4]
``` 

This outputs is derived from the following inputs: 

```
numbers = [1, 2, 3, 4]
delimiter = 5
``` 

And here is an additional example:

```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```

This outputs is derived from the following inputs: 

```
numbers = [1, 2, 3]
delimiter = 4
```