```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence."""
    return [num for num, index in sorted(enumer zip(numbers, range(len(numbers))))][::-1] # Use sorted to ensure unique values and the right order
    ```