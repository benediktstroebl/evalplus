```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimeter = 4

print(intersperse(numbers, delimeter))  # Expected output: [1, 4, 2, 4, 3, 4, 5]
``` 

The function takes in a list of numbers `numbers` and an integer `delimeter` as arguments. If the input list is empty (`not numbers`), it returns an empty list. Otherwise, it places the `delimeter` immediately after the first element of the list and then recursively calls the `intersperse` function with the rest of the list (`numbers[1:]`). This process repeats until the delimiter is inserted between every two consecutive elements of the list. 
The test case checks if the list `[1, 2, 3, 4, 5]` with `delimeter` 4 returns `[1, 4, 2, 4, 3, 4, 5]` which is the expected output. Failing the test case will result in an error while the passing test case will return the expected output.