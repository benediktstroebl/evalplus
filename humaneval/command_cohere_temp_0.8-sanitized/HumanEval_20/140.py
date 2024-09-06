from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if abs(diff) < 1e-6:  # if difference is almost zero, considering rounding errors
            return numbers[[0, -1][diff > 0]]
        else:
            return numbers[[0, -1][diff < 0]]