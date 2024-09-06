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
    if (a == b) or ((a - b) < 1e-6 and (b - a) < 1e-6):
        return a, b
    elif abs(a - b) >= abs(a - _get_closest_pair(a, a + 1e-6)) and a != b:
        return _get_closest_pair(a, a + 1e-6)
    else:
        return _get_closest_pair(b, a)