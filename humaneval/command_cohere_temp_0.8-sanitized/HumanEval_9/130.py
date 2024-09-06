from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    max_rolling = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            max_rolling[i] = numbers[i]
        elif numbers[i] < numbers[i - 1]:
            max_rolling[i] = max_rolling[i - 1]
    return max_rolling