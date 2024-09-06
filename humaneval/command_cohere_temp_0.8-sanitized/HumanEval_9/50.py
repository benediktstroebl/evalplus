from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('inf')] * rolling_window

    max_indices = [i for i, num in enumerate(numbers) if num == max(numbers[:i + rolling_window])]
    
    return [numbers[idx] for idx in max_indices]