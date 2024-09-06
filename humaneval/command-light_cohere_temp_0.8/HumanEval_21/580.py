Here is a self-contained Python script that solves the problem you described:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the list of numbers
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Test cases
test_cases = [
    [1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0.0,
   0, 1.0],
   0.2], [0, 0.0, 0.0]
[1.2, 3, 4, 5, 6]

for test_case in test_cases:
    result = rescale_to_unit(test_case)
    assert all(map(lambda x: abs(x) - 1) == [0, 1, 1, 1, 0]))
    assert all(map(lambda x: abs(x) - 0) == [0, 1, 1, 0])
    assert all(map(lambda x: x == result[0]))

print("Test cases passed!")
```