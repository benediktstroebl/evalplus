```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num > 0]
    seen.add(numbers)
    return result
```
The function removes duplicate integers from the list and returns a new list with unique positive integers. 
This solution uses the list comprehension to filter non-duplicate and non-zero numbers. The set is used to keep track of numbers already seen, and the add function is used to add numbers to the set.