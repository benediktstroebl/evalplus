```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x < numbers.count(x)]
```
The `remove_duplicates` function takes a list of integers as input and returns a new list that contains only the unique elements. It uses the `count(x)` to check if each element has already occurred before in the list, and then includes only the first occurrence of each element.