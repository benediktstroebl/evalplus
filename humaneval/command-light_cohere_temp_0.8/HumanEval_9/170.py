```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling max elements from a given list of integers.
    Each element in the
    sequence is picked as the current max element.
    Returns a max elements in order as they pick them from the list in order.
    """return [max_elements(numbers, 1)[]

test_rolling_max: List[(()), ()] = [[], [1, 2, 3, 4, 5]]
results = rolling_max(test_rolling_max)
assert all(results == [max(x) for x in test_rolling_max]) # test for all cases
print(results)
```