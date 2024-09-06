from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_length: int) -> List[int]:
    """
    Generate a list of rolling maximum elements observed in the list within rolling_length windows.
    """
    if rolling_length <= 0:
        return []

    res = [max(numbers[:rolling_length])]
    for i in range(1, len(numbers) - rolling_length + 1):
        max_window = max(numbers[i:i+rolling_length])
        res.append(max_window if max_window > res[-1] else res[-1])

    return res