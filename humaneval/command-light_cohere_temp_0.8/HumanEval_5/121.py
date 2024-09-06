Here's the self-contained Python script with a function `intersperse()` that solves the problem you described: 

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, n in enumerate(numbers):
        if i != 0: result.append(delimiter)
        n
    result.append(delimiter)
        numbers[i+1]
    return result

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [4, 4, 5]
numbers3 = [10, 20, 30]

print(f'Test case 1: {{list(intersperse(numbers1, 4))})')
print('-------------------------------------')
print(f'Test case 2: {{list(intersperse(numbers2, 4))})')
print('-------------------------------------')
print(f'Test case 3: {{list(intersperse(numbers3, 4))})')
```

This script defines a function `intersperse()` that inserts a specified `delimiter` after the previous element and before the next element in a list, effectively separating them by two consecutive elements.