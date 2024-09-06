```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list."""
    new_list = List(numbers[:])  # Create a new list with same elements and returned by []
    for i in range(1, len(numbers)):
        new_list[i] = numbers[i - 1] + delimeter
    return new_list

# Test cases
test_inserpere = [
    [
        [], 4,
        [1, 2, 3], 4,
        [10, 20, 30], 10,
        [1, 2, 3, 4, 5], 10
    ]

for test in test_inserpere:
    actual = intersperse(test, 4)
    assert actual == test, f"Expected: {test} , Got: {actual}"
```  The provided code defines a Python function called `inperse`. This function takes two parameters: `numbers`, a list of integers, and `delimiter`, an integer. The function creates a new list with the original list elements and adds a number `delimiter` between every two consecutive elements. The code uses the `List(numbers[:])` to create a new list with the same elements. The function then loops through the range(1, len(numbers)) and adds `delimiter` to the second element. The new list is then returned by the function.