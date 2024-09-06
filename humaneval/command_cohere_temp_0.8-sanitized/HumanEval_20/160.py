from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    elif len(numbers) == 2:
        return numbers[:2]
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return find_closest_elements_(left, right, numbers)
def find_closest_elements_(left: float, right: float, numbers: List[float]) -> Tuple[float, float]:
    while True:
        if len(numbers) == 0:
            return left, right
        elif numbers[0] >= left and numbers[0] <= right:
            return left, right
        elif numbers[0] < left:
            left = numbers.pop(0)
        else:
            right = numbers.pop(-1)