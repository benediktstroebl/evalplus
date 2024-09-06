```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

numbers = [1, 2, 3, 2, 4, 2, 1]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```
This script defines a function remove_duplicates that takes a list of integers as input and returns a new list that contains only the unique elements after removing duplicates. The function uses the time complexity of `O(n)` and the space complexity of `O(1)` since it creates a set and then converts it to a list. The set operations are usually considered to be constant on average, and the conversion from set to list takes constant time.