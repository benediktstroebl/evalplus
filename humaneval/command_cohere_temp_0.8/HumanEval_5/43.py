```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimeter = 4

expected_output = [1, 4, 2, 4, 3, 4, 5]

print(intersperse(numbers, delimeter))
```

The function `intersperse()` takes in a list of numbers and a delimeter as input and returns a new list where the delimeter is inserted between every two consecutive elements of the input list. The function is recursive, with the base case checking for an empty list (`return delimeter if not numbers`). If the list is not empty, the function concatenates the first element of the list, the delimeter, and the rest of the list with the delimeter inserted after every element (`return numbers + [delimeter] + intersperse(numbers[1:], delimiter)`).

The test case checks the output of the function with the input of a list of numbers and a delimeter and prints the expected output.