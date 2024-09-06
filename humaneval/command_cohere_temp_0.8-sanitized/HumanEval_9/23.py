from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    given moment in the sequence. Maximum elements overlapping with the rolling_max_window are included."""
    rolling_maxes = [float('-inf')] * rolling_max_window
    curr_max = 0
    
    for num in numbers:
        if num > curr_max:
            curr_max = num
            index = 0
            while index < rolling_max_window and rolling_maxes[index] > curr_max:
                rolling_maxes[index] = curr_max
                index += 1
        elif index < rolling_max_window and num == rolling_maxes[index]:
            index += 1
    
    return rolling_maxes