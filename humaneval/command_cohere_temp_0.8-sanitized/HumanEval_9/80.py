from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[0][1: rolling_window + 1]) 
             for numbers in zip(numbers, numbers[1:])[0: -rolling_window - 1:-1]]
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3