from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_length: int) -> List[int]:
    """
    Generate a list of rolling maximum elements observed in the list within rolling_length windows.
    """
    if rolling_length <= 0:
        return []

    res = [max(window) for window in zip_longest(*[iter(numbers)]*rolling_length, fillvalue=float('-inf'))]
    return res