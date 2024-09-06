```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code snippet takes a list of values of any type as input and returns a list of integers. It uses a list comprehension to iterate over each element in the input list and checks if the element is an instance of the int class, and then assigns it to the result list. Finally, it returns the result list, which contains all the integers from the original list. The function efficiently filters out non-integer elements and only returns the integers present in the input list.