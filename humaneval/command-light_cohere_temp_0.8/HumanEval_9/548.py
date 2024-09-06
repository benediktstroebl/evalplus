```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements found in the sequence.
    Each element in the rolling-max sequence is the maximum value seen 
    up to that moment in the original sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Initialize first and last elements
    max_element = numbers[0]
    rolling_max_elements = [max_element]

    # Move the window one step ahead in the sequence
    for num in numbers[1:]:
        current = num
        new_max = max_element
        for n in rolling_max_elements:
            if n > current:
                new_max = n
        max_element = new_max
        rolling_max_elements.push_back(new_max)

    return rolling_max_elements
```