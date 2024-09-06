from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    elif len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        middle = numbers[(len(numbers) + 1) // 2]
        left, right = numbers[::2], numbers[1::2]
        return _closest_two_elements(middle, left, right)
def _closest_two_elements(element: float, left_numbers: List[float], right_numbers: List[float]) -> Tuple[float, float]:
    left_idx = right_idx = 0
    min_distance = float('inf')
    for i in range(len(left_numbers)):
        dist = abs(left_numbers[i] - element)
        if dist < min_distance:
            min_distance = dist
            left_idx = i
    for i in range(len(right_numbers)):
        dist = abs(right_numbers[i] - element)
        if dist < min_distance:
            min_distance = dist
            right_idx = i
    return left_numbers[left_idx], right_numbers[right_idx]