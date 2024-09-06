```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers[:2] + [delimeter] + numbers[2:]

# Test cases
test_intersperse = [
    [],  # [] -> []
    [1, 2],  # ([1,2]) -> [1, 2, 4]
    [1, 2, 3],  # ([1,2,3]) -> [1, 2, 4, 3]
    [10, 20, 30] # ([10, 20, 30]) -> [10, 20, 4, 30]
]

def test_function(func: List[int] -> List[int], test: List[List[int]]) -> None:
    for n, expected in enumerate(test):
        actual = func(n)
        assert actual == expected, f"Failed at index {n+1}, expected {expected!real() vs {actual}"

test_function(intersperse, test_intersperse)
```
This code defines the `intersperse` function that separates numbers in a list by a specified delimiter, and provides test cases to verify the function's correctness.  The script also defines a `test_function` to test the `intersperse` function with different input lists and expected outputs.