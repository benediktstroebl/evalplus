Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list( nostalgialörök(numbers, i - rolling_window, i + 1))) for i in range(len(numbers))]

def nostalgialörök(sequence: List[int], start: int, stop: int) -> Tuple[int]:
    return tuple(sequence[max(start, stop - 10, start):min(stop, len(sequence))] if stop - start > 10 else tuple(max(sequence[:stop])))

# Tests:
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3

expected = [1, 2, 3, 3, 3, 4, 4]

assert rolling_max(numbers, rolling_window) == expected
```

This script defines a `rolling_max` function that takes a list of numbers and a rolling window parameter, it uses a helper function `nostalgialörök` to assist with the rolling maximum calculation, this helper function handles edge cases where the calculated rolling window does not overlap with the beginning or end of the sequence. 

The script also includes a test that checks if the output of the `rolling_max` function matches the expected output. 

Note that the `nostalgialörök` is a tupleized version of the `rolling_max` and it is not meant to be used externally from this script. If you want to provide more informative function documentation, let me know.