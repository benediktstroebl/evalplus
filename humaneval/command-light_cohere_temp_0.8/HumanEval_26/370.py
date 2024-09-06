```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = [x for x in numbers if numbers.count(x) == 1]
    return result
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]
``` 
The function removes duplicates from a list of integers and returns the result.