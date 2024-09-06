```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimiter)
    result.append(num)
    return result

# Test
test_numbers = [1, 2, 3,4]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)
``` 
This code is a complete Python program that implements the "**`intersperse`**" function, which inserts a specified delimiter between every two consecutive elements in an input list. It uses this "**`from_ typing`**" to ensure proper types and provides a simple test using a sample input list and delimiter value.