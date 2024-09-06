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
    if (b - a) < (a - b):
        closer, farther = a, b
    else:
        closer, farther = b, a
    if abs(closer - farther) > 1e-6:
        return closer, farther
    else:
        middle = (a + b) / 2
        return _get_closest_pair(closer, middle)