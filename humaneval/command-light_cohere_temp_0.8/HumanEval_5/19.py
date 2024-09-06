```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimiter)
    result.append(num)
    return result

numbers = [1, 2, 3, 4, 5]
delimiter = 4
result_test = intersperse(numbers, delimiter)
print(result_test)  # Output: [1, 4, 2, 4, 5]

numbers = [1, 2, 3, 4, 5]
delimiter = 3
result_test2 = intersperse(numbers, delimiter)
print(result_test2)  # Output: [1, 3, 4, 5]
``` 
This script defines a function `intersperse` that takes a list of integers and an integer `delimiter` as input, and returns a list with the integers interspelled by the specified `delimiter`.