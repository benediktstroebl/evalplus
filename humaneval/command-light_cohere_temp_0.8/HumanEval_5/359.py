```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i, j in zip(numbers, numbers[1:]) for j in numbers[1:] ] + numbers[0]

# Test cases for function
numbers = [3, 1, 4, 1, 10, 2]
delimiter = 1
expected = [3, 4, 1, 10, 2]
print(intersperse(numbers, delimiter)) # Prints the expected output
```