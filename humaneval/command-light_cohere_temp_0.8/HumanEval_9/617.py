```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generates a list of rolling maximum elements in a given list of integers.
    Args:
        - numbers (List[int]) -> The list of integers.
    Returns: list of integers (List[int]) 
    containing the rolling maximum elements in the given list.
    """

rolling_max([1,2,3,2,3,4,2]) # [1, 2, 3, 3, 3, 4] 
    ```