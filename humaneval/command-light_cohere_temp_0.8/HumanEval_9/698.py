```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return the list of rolling maximum elements in the given sequence.
    """
    def rolling_max_sequence(sequence: List[int]) -> List[int]:
        max_so_far = sequence[0]
        result = [sequence[0]]
        for num in sequence[1:]:
            if num > max_so_far:
                max_so_far = num
                result.append(max_so_far)
            else:
                result.append(num)
        return result
    """
    # Example usage
    sequence = [1, 2, 3, 2, 3, 4, 2]
    result = rolling_max_sequence(sequence)
    return result
```