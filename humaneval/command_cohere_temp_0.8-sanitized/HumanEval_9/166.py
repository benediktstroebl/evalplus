from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    return [max(subsequence) for subsequence in zip_longest(*([iter(numbers)] * rolling_window), fillvalue=float('-inf'))]
numbers = [1, 2, 3, 2, 3, 4, 2]