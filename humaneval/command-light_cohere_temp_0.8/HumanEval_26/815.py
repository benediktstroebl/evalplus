```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n < numbers.count(n)]
```
This function uses the list comprehension technique to create a new list that contains only the unique integers from the input list. It uses the specific function `count()` that returns the number of occurrences of an element in a list. The `if` statement is used to filter out the duplicates.