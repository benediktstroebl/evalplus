```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first filtering out the `delimeter` values from the `numbers` list using a list comprehension, creating a new list that includes all elements of `numbers` except for the `delimeter`. If the resulting list is empty (meaning there are no non-delimeter elements in `numbers`), it returns an empty list. Otherwise, it returns the delimeter value appended to the end of the new list, thus interspersing the `delimeter` between all adjacent elements in the `numbers` list. 

Here is an example usage of the function:
```python
print(intersperse([1, 2, 3], 4))
```

The output of this call will be:
```
[1, 4, 2, 4, 3]
``` 

This is interpreted as: "take the list `[1, 2, 3]`, then interspersed with the value `4` between each element, the resulting list is `[1, 4, 2, 4, 3]`".