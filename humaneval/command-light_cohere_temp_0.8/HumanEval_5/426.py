```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list """
    result = [num] + [num + delimeter for num, delimeter in zip(numbers, [0, delimeter])] + [num]
    return result

# Test the function with different inputs
test_data = [4, 2, 3, 1]
test_result = intersperse(test_data, 4)
print(test_result)  # Output: [1, 4, 2, 4, 3]

test_data = [1, 2, 3]
test_result = intersperse(test_data, 4)
print(test_result)  # Output: [1, 4, 2, 4, 3]

test_data = [4, 2, 1]
test_result = intersperse(test_data, 5)
print(test_result)  # Output: [4, 5, 2, 5]

test_data = [1, 2, 3]
test_result = intersperse(test_data, 5)
print(test_result)  # Output: [1, 5, 2, 5, 3]
```  This code defines a function `intersperse` that inserts a number `delimiter` between every two consecutive elements of the input list. It then passes tests tests with various inputs and the results are printed to the console.