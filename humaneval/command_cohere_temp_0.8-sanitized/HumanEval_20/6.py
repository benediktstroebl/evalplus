from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    if delta > 0.00001:
        return numbers[-1], numbers[0]
    else:
        return numbers[1], numbers[0]