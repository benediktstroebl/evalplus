from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[0][1:rolling_window+1]) 
             for numbers in zip(*[iter(numbers)]*rolling_window)]