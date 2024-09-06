```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.find()]  #{num}]

# Test the function with markdown code block input
numbers = [1, 2, 3, 2, 4, 1, 4]
print(remove_duplicates(numbers))
```