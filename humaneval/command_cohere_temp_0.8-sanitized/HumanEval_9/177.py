from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """Return a list of rolling maximum elements found in the list of numbers over rolling_window size windows."""
    # Initialize output list with max(list)
    out = [max(numbers[:rolling_window])]
    # Iterate through list, keeping track of maximum element and updating rolling max
    for i in range(len(numbers)-rolling_window+1): 
        current_max = max(numbers[i:i+rolling_window])
        out.append(current_max)
    return out
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3