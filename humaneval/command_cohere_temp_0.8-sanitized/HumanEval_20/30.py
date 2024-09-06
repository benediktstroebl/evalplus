from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    elif len(numbers) == 2:
        return numbers[:2]
    else:
        middle = numbers[(len(numbers) + 1) // 2 - 1]
        left, right = numbers[:len(numbers) // 2], numbers[len(numbers) // 2:]
        return _find_closest(left, right, middle)
def _find_closest(left: List[float], right: List[float], middle: float) -> Tuple[float, float]:
    left_idx = left.index(middle) + 1
    right_idx = right.index(middle) + 1
    if left_idx > right_idx:
        left, right = right, left
        left_idx, right_idx = right_idx, left_idx
    return left[left_idx - 1], right[right_idx - 1]