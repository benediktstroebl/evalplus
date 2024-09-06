```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n < numbers.count(n)]
```
This function utilizes the List comprehension and the count() function to remove any duplicate numbers from the input list.