Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found up to that point in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [float('-inf')] * len(numbers)
    rolling_maxes[0] = numbers[0]
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[i] > numbers[j] : 
                rolling_maxes[i] = max(rolling_maxes[i], rolling_maxes[j]) 
        rolling_maxes[i] = max(rolling_maxes[i], numbers[i])
    return rolling_maxes
```

The algorithm for the above function operates by initializing a list `rolling_maxes` with as many elements as the input list, filling it with `-inf` values. For each element in the input list, it iterates through the previous elements and maximizes the `rolling_maxes` list accordingly.

Here is an example usage of the function to test it against the provided test case:
```python
test_cases = [
    ([1, 2, 3, 2, 3, 4, 2], [1, 2, 3, 3, 3, 4, 4]),
    ([1], [1]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 4, 3], [1, 2, 4, 4, 4]),
    ([1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1])
]

for test_case in test_cases:
    numbers, expected = test_case
    output = rolling_max(numbers)
    assert output == expected
```

This will ensure the function behaves as expected against a variety of input test cases.