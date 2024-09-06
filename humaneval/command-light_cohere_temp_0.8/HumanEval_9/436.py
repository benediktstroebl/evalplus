```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates the maximum element found in a list, and returns the rolling maximum sequence until a given moment.
    >>> [1, 2, 3, 2, 3, 4, 2]
    >  rolling_max([1, 2, 3, 2, 3, 4, 2])
    [2, 3, 3, 3, 3, 4]
    """
    # Initialize the rolling_max list with the first element, which is also the maximum.
    rolling_max.append(numbers[0]
    # Loop through the sequence
    for num in numbers[1:]:
        # Update the current maximum element.
        if num > rolling_max[-1]:
            rolling_max[-1] = num
        # Append the current maximum element to the rolling_max list.
        rolling_max.append(num)
    done.
    return rolling_max
done
```