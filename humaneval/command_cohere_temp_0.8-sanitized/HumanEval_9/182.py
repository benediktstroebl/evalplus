from typing import List, Tuple
def rolling_max(numbers: List[int], max_window: int = None) -> List[int]:
    if max_window is None:
        max_window = len(numbers)

    rolling_max_values = [numbers[0]]

    for i in range(1, len(numbers)):
        if i - max_window < 0:
            rolling_max_values.append(numbers[i])
        else:
            rolling_max_values.append(max(rolling_max_values[-max_window: i + 1]))

    return rolling_max_values