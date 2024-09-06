from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    return numbers[0], numbers[-1] if delta == 0 else numbers[1] + (0.0 if delta > 0 else 1e-6)
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]