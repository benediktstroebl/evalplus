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
    if (a == b) or ((a + b) / 2.0 in [x for x in [a, b] if x != 0.0]):
        return a, b
    else:
        return _get_closest_pair(a, b - (b - a)) if a != b else a, a