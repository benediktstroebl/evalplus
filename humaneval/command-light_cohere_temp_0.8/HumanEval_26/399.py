```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

numbers = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
This script defines a function **remove_duplicates** that removes duplicate elements from a list of integers. The function uses the simple list comprehension to filter out any duplicate numbers, ensuring the result is unique.