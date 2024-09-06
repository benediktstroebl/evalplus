Here is a Python script that includes a self-contained function that solves the problem of inserting a number 'delimiter' between every two consecutive elements in the input list:
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter <= 2] + [num for _, delimeter in enumerate(numbers) if delimeter > 2]

# Test cases
test_cases = [
    [], 4,
    [1, 2, 3], 4,
    [10, 20, 30], 10, 40, 50, 60
]

for case in test_cases:
    print(case, end=' ')
    print(intersperse(case))
    print()
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a list of integers with the delimiter inserted between every two consecutive elements. The script then provides a test cases, and the `intersperse` function is called for each test case. The output will display the result of each test case.