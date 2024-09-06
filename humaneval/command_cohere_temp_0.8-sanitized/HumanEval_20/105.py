from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    elif len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        middle = numbers[len(numbers) // 2]
        last_idx = len(numbers) - 1
        return sorted([middle, numbers[last_idx]])[::-1]