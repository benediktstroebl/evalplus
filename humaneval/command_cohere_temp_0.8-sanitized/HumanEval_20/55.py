from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    return numbers[0], numbers[-1] if delta == 0 else numbers[0] + delta / 2.0