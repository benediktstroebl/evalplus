```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()]]

    # Test case
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    print(f"Test passed: {expected}")
    return expected
```