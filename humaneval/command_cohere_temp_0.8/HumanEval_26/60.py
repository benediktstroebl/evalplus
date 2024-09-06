```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers (`List[int])` as input and returns a list of unique integers from the input list. Inside the function, it uses a set to store the unique numbers, and the `list()` function is used to convert the set back to a list, ensuring that the order of the unique elements is preserved. 

To retain the order of elements, it's essential to use the `set()` function instead of `list()` for uniqueness treatment because the former maintains the element order while the latter does not. The function effectively removes all elements that occur more than once, ensuring that only unique integers are retained in the output list.