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
        return find_closest_elements__(left, right, numbers)
def find_closest_elements__(left: float, right: float, numbers: List[float]) -> Tuple[float, float]:
    while numbers.count(left) > 1 or numbers.count(right) > 1:
        if numbers[::2].count(left) == 1 and numbers[1::2].count(right) == 1:
            left, right = numbers[::2].index(left), numbers[1::2].index(right)
        else:
            left, right = right, left
    return left, right