```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[0]]


# Test
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # expected output: [1, 3, 4]
``` 
I hope this helps you with your problem!