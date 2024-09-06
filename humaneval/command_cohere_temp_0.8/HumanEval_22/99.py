```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out values that are not integers. It does so by iterating through each value in the input list and checking if the current value is an instance of the integer class using the `isinstance` function. If it is, the value is appended to the `result` list, which is returned once all values have been processed. 

This approach ensures that only actual integers are included in the output, regardless of whether other types of values are present in the input list.