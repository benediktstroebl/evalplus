```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The approach used in the function `remove_duplicates` is to iterate over the input list `numbers` and maintain a `set` called `seen` to keep track of unique elements. For each element `num` in `numbers`, it checks whether `num` is not in `seen` or if the size of `seen` is 1, indicating the first occurrence of an element. If either of these conditions is met, it adds `num` to the `result` list and updates `seen` to mark `num` as seen. Elements that have been seen before are skipped.

This approach results in the output of the function removing duplicate elements from the input list while preserving the order of the remaining elements. 

To validate the functionality of the script, you can create a test case like the one provided in the original problem statement:
```python
test_cases = [
    ([1, 2, 3, 2, 4], [1, 3, 4]),
    ([1, 2, 3, 4, 4, 5], [1, 2, 3, 5]),
    ([1, 3, 1, 5, 4, 4, 6, 7, 6, 1, 8, 9, 9, 8, 1], [1, 3, 5, 6, 7, 8, 9])
]

for test_case, expected in test_cases:
    result = remove_duplicates(test_case)
    assert result == expected
```

In this validation code, multiple test cases are defined as lists of input lists (`test_case`) along with the expected output (`expected`). The `remove_duplicates` function is applied to each input list in the test case, and the resulting list is compared against the expected output using the `assert` statement.