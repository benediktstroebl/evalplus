```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements found until a given moment in the sequence.
    :Args:
        numbers: list[int]
    """
    # Initialize the rolling window
    rolling_max_elements = [num for num in numbers]
    rolling_max_elements.append(max(rolling_max_elements))
    return rolling_max_elements

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 3, 4, 2]
    print("Rolling Maximum Elements:", rolling_max(numbers))
```