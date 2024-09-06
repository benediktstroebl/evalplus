```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimiter in zip(numbers, [delimeter] * 2)]

# Test the function with sample inputs and assertions
numbers = [4, 1, 2, 3]
delimiter = 4

expected = [4, 8, 12, 16]
assert intersperse(numbers, delimiter) == expected

# Another test with a different list and delimiter values
numbers2 = [1, 2, 3]
delimiter2 = 4

expected2 = [5, 9, 13]
assert intersperse(numbers2, delimiter2) == expected2
```