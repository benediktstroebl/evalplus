```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num < numbers.count(num)]
```
The function creates a new list with all elements from the input list that appear only once, using the `count()` function to check if each element appears more than once.