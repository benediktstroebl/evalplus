```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[0]]

# Unit tests
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates = [
    "remove_duplicates should return a list containing integers that occur at most once.",
    "input() should return [1, 3, 4]",
]

result = remove_duplicates(numbers)
test_remove_duplicates(result)

```