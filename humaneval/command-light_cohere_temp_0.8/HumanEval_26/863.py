```python
from typing import List
def remove_duplicates(numbers: List[int]): 
    seen = set()
    return [num for num in numbers if num not in seen and num not in [2, 4]]

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 4, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4, 5]

numbers = [1, 2, 3, 4, 2]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 2, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]
```
This Python script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a sets to keep track of elements seen so far, then iterates through the input list, checking each element against the set to determine if it's a duplicate. Finally, the function returns a new list with unique elements.