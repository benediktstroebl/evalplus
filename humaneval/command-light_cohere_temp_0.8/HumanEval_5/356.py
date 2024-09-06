```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases are self-contained within the script
test_case1 = [1, 2, 3]
test_case2 = [4, 4, 4]
test_case3 = [4, 1, 4]
test_case4 = [1, 2, 4, 3, 4]

print(f"Test case 1 results: {formatDelimiter ',')
print(intersperse(test_case1, 4))
print('}')

print(f"Test case 2 results: {formatDelimiter ',')
print(intersperse(test_case2, 4))
print('}')

print(f"Test case 3 results: {formatDelimiter ',')
print(intersperse(test_case3, 4))
print('}')

print(f"Test case 4 results: {formatDelimiter ',')
print(intersperse(test_case4, 4))
print('}')
```