```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num < len(numbers) and numbers.re same(num)]
```
The remove_duplicates function takes a list of integers as input and returns a new list with all distinct integers from the original list. It achieves this by using a list comprehension and the same function, which checks if an element is already in the list. This ensures that each number is only added to the result if it is not already present in the list.