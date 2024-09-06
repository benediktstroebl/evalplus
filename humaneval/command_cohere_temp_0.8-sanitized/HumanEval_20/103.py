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
    if (b - a) <= 1e-6:
        return a, b
    elif abs(a - b) == abs(b - a):
        return a, b
    elif a == b:
        return a, b
    else:
        if a > b:
            a, b = b, a
        return _get_closest_pair(a, a + (b - a) / 2)