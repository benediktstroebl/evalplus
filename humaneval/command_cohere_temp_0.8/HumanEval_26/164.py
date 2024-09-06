```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers (`numbers`) as input. It uses a set to automatically filter out any duplicate elements from the input list and then converts this set back into a list, returning the result. As a result, the function removes all duplicate occurrences of integers while preserving the original order of unique elements, ensuring that each output list contains only unique integers from the input list.