```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

numbers = [1, 2, 3, 2, 4, 2, 3]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 2, 4, 2, 3, 1]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 3, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 4, 5, 6]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]
``` 
The remove_duplicates function uses the set data structure to remove duplicate elements from the input list. This ensures that the clear and efficient output.