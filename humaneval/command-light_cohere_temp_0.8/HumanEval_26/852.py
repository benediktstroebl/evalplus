```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.find()]]

numbers = [1, 2, 3, 2, 4, 3, 1, 4]
print(remove_duplicates(numbers))
```
This code defines a function **`remove_duplicates`** that takes a list of integers as input and returns a new list with all distinct integers from the original list. The code then demonstrates the unique behavior by creating a list of numbers and then calling the **`remove_duplicates`** function with this list. The expected output is `[1, 2, 3, 4]`.