```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n not in set(numbers)]

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
``` 
This function uses the set data structure to remove duplicate integers from the input list, and then re-instantiates the list with the filtered values.