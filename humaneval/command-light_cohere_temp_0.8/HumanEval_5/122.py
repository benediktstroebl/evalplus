```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list """
    result = [num] + [num + delimeter for num, delimeter in zip(numbers, [0, delimeter])] + [num]
    return result

# Test case 1
numbers = [1, 2, 3]
result1 = intersperse(numbers, 4)
assert len(result1) == 6
assert all(map(float, result1)) == [1.4, 2.0, 4..8, 3,  #4, 4, 3]

# Test case 2
numbers = [1, 2, 3, 4, 5]
result2 = intersperse(numbers, 3)
assert len(result2) == 7
assert all(map(float, result2)) == [1.0, 2.0, 3.0, 4.8, 5]
 3, 5]

# Test case 3
numbers = [1, 2, 3, 4, 5, 6]
result3 = intersperse(numbers, 2)
assert len(result3) == 9
assert all(map(float, result3)) == [1.0, 2.0, 3.0, 4.2, 4.0, 5, 6]
```  The code defines a function `intersperse` that inserts a number `delimeter` between every two consecutive elements of an list. The `typing` module is used to specify the `List` types for the input and output of the `intersperse` function. The test cases demonstrate the expected behavior of the `intersperse` function.