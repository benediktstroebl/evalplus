```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.get(0)]]

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 4]
result = remove_duplicates(numbers)
print(result)
# expected output: [1, 3, 4]

numbers = [1, 2, 2, 3, 4, 3]
result = remove_duplicates(numbers)
print(result)
# expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5]
result = remove_duplicates(numbers)
print(result)
# expected output: [1, 2, 3, 4]
```