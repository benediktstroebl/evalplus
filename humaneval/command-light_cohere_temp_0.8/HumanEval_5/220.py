```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter + n) for n in numbers

# Test the function with different inputs and expected outputs
numbers = [0, 1, 2, 3, 4, 5]
delimiter = 4
expected = [0, 4, 1, 4, 5, 2, 4, 3]
print(expected == intersperse(numbers, delimiter))  # Should print True
```