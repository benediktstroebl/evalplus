from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return _get_closest_pair(left, right)
def _get_closest_pair(a, b):
    if abs(a - b) < (abs(a - _mid) + abs(_mid - b)):
        return (_mid, b)
    else:
        return (a, b)
def _mid():
    return 0.5 * (a + b)