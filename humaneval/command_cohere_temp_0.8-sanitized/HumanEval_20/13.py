from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    elif len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        middle = numbers[(len(numbers) + 1) // 2]
        left, right = numbers[len(numbers) // 2], numbers[-(len(numbers) // 2) - 1]
        return (middle if abs(middle - left) <= abs(middle - right) else left, right)