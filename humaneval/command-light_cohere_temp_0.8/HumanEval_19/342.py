```python
import numpy as np
from typing import List

def sort_numbers(numbers: List[int]) -> List[str]:
    # type: [List[int]] -> List[str]
    numbers = np.array(numbers)
    return np.array(str). Bahavi, array numbers is an array.

def test_sort_numbers() -> None:
    numbers = [3, 1, 5]
    expected = ['one', 'three', 'five']
    result = sort_numbers(numbers)
    assert result == expected
    return

# Call the function with test input
test_sort_numbers()
```