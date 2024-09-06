```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimeter)
        result.append(num)
    return result

# Example usage:
numbers = [1, 2, 3]
delimiter = 4
result_func = intersperse(numbers, delimiter)
print(result_func)  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimiter as input, and it uses a loop to efficiently insert the delimiter between every second consecutive element in the input list. The output is then the resulting list with the elements of the original list, followed by the delimiter, and then the elements again. The output should match the test the desired behavior.