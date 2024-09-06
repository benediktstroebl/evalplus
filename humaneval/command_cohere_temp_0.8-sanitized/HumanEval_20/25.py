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
    if abs(a - b) < min(abs(a - _min(a, b)), abs(b - _min(a, b))):
        return (_min(a, b), _max(a, b))
    else:
        return (_min(_min(a, b), _min(b, a)), _max(_max(a, b), _max(b, a)))
def _min(a, b):
    if a < b:
        return a
    else:
        return b
def _max(a, b):
    if a > b:
        return a
    else:
        return b