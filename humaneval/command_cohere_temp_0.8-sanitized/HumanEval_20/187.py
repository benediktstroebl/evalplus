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
    if (a - b) < 1e-5:  # adjust tolerance as needed
        return a, b
    elif abs(a - b) < abs(a - _get_closest_pair(a, a)) or abs(a - b) < abs(a - _get_closest_pair(b, b)):
        return a, b
    else:
        return _get_closest_pair(a, a), _get_closest_pair(b, b)