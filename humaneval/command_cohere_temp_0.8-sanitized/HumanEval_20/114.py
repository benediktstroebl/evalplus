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
    if (a - b) < 1e-6:  # adjust the threshold as needed
        return a, b
    elif abs(a - b) == min(abs(a - c) for c in numbers) or abs(a - b) == min(abs(b - c) for c in numbers):
        return a, b
    else:
        return _get_closest_pair(a, numbers[1]) if abs(a - numbers[1]) < 1e-6 else _get_closest_pair(numbers[0], b)