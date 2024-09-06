```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It uses list comprehension to filter out the `delimeter` tokens from the `numbers` list and then constructs the resulting list by adding `delimeter` to the end of the filtered list. The added `delimeter` is used to correctly terminate the list if the input list is shorter, ensuring that the result is a properly interspersed list or an empty list if the input list is empty or consists only of `delimeter` tokens. 

Here is a simple test case to test the above function:
```python
test_cases = [
    ([], 4, []),
    ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
    ([1, 2, 3, 4], 5, [1, 5, 2, 5, 3, 5, 4]),
    ([1, 1, 3, 3, 4, 4], 0, [1, 0, 3, 0, 4, 0]),
    (list(range(10)), 2, list(range(2, 12, 2))),
]

for nums, delim, want in test_cases:
    assert intersperse(nums, delim) == want
```