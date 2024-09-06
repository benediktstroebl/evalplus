```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Compute the rolling maximum element in a sequence, returning the maximum value seen so far 
    and the index of its occurrence.
    """
    elements of expected to be a list of integers
    """
    current = numbers[0]
    seen = [current]

    for num in numbers[1:]:
        # Update current if seeing a greater number
        if num > current:
            current = num
        # Add current number to the set of seen numbers
        seen.append(current)

    # Return the list of seen numbers up to the maximum value seen so far
    return seen
```