```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements found until a given moment in the sequence.
    Each element in the max sequence is calculated and returned.
    """param start Moment": int, "Starting moment"
    """
    # Initialize the rolling max list
    rolling_max = [startMoment]

    while numbers:
        currentMoment = numbers[0]
        # Move the elements of the list that is less than currentMoment to the tail
        numbers.remove(sorted(numbers, key=lambda x: x < currentMoment))

        # Append the current maximum element
        rolling_max.append(currentMoment)

        # Move to the next element
        numbers.append(numbers.pop(0))
        numbers = numbers[1:]

    return rolling_max
```