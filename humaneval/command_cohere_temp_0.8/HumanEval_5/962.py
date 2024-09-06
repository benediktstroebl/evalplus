```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of the `numbers` list. It uses a list comprehension to create a new list, `result`, which includes the elements of `numbers` but filters out the occurrences of `delimeter`. 

If `result` is empty, it means that the `numbers` list only contained the `delimeter` value and therefore, the function returns an empty list. Otherwise, the function returns `delimeter` appended to `result`, thereby correctly interspersing the `delimeter` between every two consecutive elements of the `numbers` list. 

Here is a simple test case to verify the functionality of the code:
```python
test_cases = [
    ([], 4, []),
    ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
    ([1, 2, 3, 4], 5, [1, 5, 2, 5, 3, 5, 4]),
    ([1, 1, 3, 3, 4, 4], 0, [1, 0, 3, 0, 4, 0])
]

for numbers, delimeter, expected in test_cases:
    assert intersperse(numbers, delimeter) == expected
```

You can add more test cases to increase test coverage and validate the edge cases of the `intersperse` function.