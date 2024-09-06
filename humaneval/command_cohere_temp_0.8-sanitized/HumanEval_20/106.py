from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    elif len(numbers) == 2:
        return numbers[:2]
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return find_closest_elements_(left, right, numbers)
def find_closest_elements_(left: float, right: float, numbers: List[float]) -> Tuple[float, float]:
    while left != right:
        if abs(left - right) < abs(left - numbers[1]) and abs(left - right) < abs(right - numbers[0]):
            right = numbers[0]
        else:
            left = numbers[1]
        numbers = numbers[1:] + numbers[:1]
    return left, right