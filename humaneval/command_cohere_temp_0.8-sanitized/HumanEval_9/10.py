from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found in the sequence."""
    rolling_max_return = []

    for i in range(len(numbers)):
        current_max = max(numbers[i:i+2])
        if i == 0:
            rolling_max_return.append(numbers[i])
        else:
            rolling_max_return.append(current_max)

    return rolling_max_return
numbers = [1, 2, 3, 2, 3, 4, 2]