Here's the Python script with the self-contained function `remove_duplicates()`:

```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps only the _ elements left as in the input.
    return [set of numbers[0] to remove duplicates
    """
    seen = set(numbers)
    result = [num for num in numbers if num not in seen]
    return result
```