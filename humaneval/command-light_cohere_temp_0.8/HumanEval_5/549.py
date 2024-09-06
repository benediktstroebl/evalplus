Here is a self-contained Python script that solves the problem of inserting a number `delimiter` between every two consecutive elements of the input list:
```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]+delimeter)
        else:
            result.append(numbers[i])
    return result
```
The function takes a list of integers `numbers` and a delimiter `delimiter` as input. It then iterates through list and adds the `delimiter` to every other element except for the first and last, which it appends the original element.