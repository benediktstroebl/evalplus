```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers (`List[int])` as input and returns a list of unique integers from the input list. Inside the function, it uses a set, which inherently only stores unique elements, to filter out any duplicate integers in the input list. Thus, it solves the problem by removing duplicates and returning a list of unique integers while maintaining the order of the remaining elements.