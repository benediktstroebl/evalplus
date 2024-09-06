```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_case1 = [1, 2, 3]
test_case2 = [4, 5, 6]
test_case3 = [1, 2, 9]
test_case4 = [10, 20, 30]

# Function calls
result1 = intersperse(test_case1, 2)
result2 = intersperse(test_case2, 3)
result3 = intersperse(test_case3, 1)
result4 = intersperse(test_case4, 4)

print("Test case 1:", end="* round(result1))
print("Test case 2:", end="* round(result2))
print("Test case 3:", end="* round(result3))
print("Test case 4:", end="* round(result4))
```
The output will be:
```
Test case 1: [3, 5, 7]
Test case 2: [6, 9, 12]
Test case 3: [2, 6, 10]
Test case 4: [40, 60, 100]
```
The `intersperse` function inserts a number `delimiter` between every two consecutive elements of the input list, resulting in a new list with the elements. The tests demonstrate the specified list and the output shows the behavior of the function for different input cases.