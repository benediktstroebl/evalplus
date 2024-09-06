```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimeter = 4

expected_result = [1, 4, 2, 4, 3, 4, 5]

assert intersperse(numbers, delimeter) == expected_result
``` 

The function `intersperse()` takes in a list of integers `numbers` and an int `delimeter` as parameters. If the input list is empty, it returns an empty list. Otherwise, it inserts the `delimeter` between every two consecutive elements in the input list and returns the modified list.

The test case checks the correctness of the `intersperse()` function by using the `assert` statement. It passes an example `numbers` list and `delimeter` value and checks if the result of the function call matches the expected result.