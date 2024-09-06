from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    else:
        diff = numbers[-1] - numbers[0]
        if diff < 0:
            # Swap the first and last numbers
            numbers[0], numbers[-1] = numbers[-1], numbers[0]
        return numbers[0], numbers[-1]