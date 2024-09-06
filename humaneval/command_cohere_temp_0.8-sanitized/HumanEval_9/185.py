from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    out = [num for num in numbers if not numbers[num:]] + max(numbers[1:])
    return [x for x in out if x != max(numbers)]