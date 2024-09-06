from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found in the sequence."""
    rolling_max_return = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_max_return[i] = numbers[i]
    return rolling_max_return