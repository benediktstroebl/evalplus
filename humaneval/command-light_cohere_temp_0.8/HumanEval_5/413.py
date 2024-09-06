```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test cases
test_empty = []
test_single = [1]
test_double = [1, 2, 3]
test_triple = [1, 2, 3, 4, 5]
test_lists = [1, 2, 3], [4, 5, 6], [7, 8, 9]

# Test results
test_empty_result = intersperse(test_empty, 4)
print("Test Empty:", test_empty_result)
test_single_result = intersperse(test_single, 4)
print("Test Single:", test_single_result)
test_double_result = intersperse(test_double, 4)
print("Test Double:", test_double_result)
test_triple_result = intersperse(test_triple, 4)
print("Test Triple:", test_triple_result)
test_lists_result = intersperse(test_lists, 4)
print("Test Lists:", test_lists_result)
```
This code defines a function ` interspersed` that inserts a separator number between every second element of a given list. The provided test cases and results are printed.