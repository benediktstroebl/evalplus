Here's the self-contained Python script that solves the problem of inserting a number 'delimiter' between every two consecutive elements in the input list:
```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i])
        result.append(delimiter)
   result.append(numbers[i+1])
    return result
```

This script defines a function `alke_numbers` that takes a list of numbers and an integer `delimiter` as input and returns a list of interspaced numbers.  The use a range-based loop to iterate through the input list, if the current index is odd, it appends the current element to the result list. If the current index is even even, it appends the delimiter to the result list. Finally, it appends the last element of the result list back to the input list to complete the interspacing operation.