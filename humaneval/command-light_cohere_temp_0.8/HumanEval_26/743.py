```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num < len(numbers) and num not in numbers[numbers.keys]]
```
numbers = [1, 2, 3, 2, 4, 2, 3]
print(remove_duplicates(numbers))
``` 
This code implements the remove_duplicates function, which accepts a list of integers and outputs a new list with all distinct integers from the input. This is by iterating over the list and checking for duplicates, the code effectively removes all duplicates and returns the resulting unique list.