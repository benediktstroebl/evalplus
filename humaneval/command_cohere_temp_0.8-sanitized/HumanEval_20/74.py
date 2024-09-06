from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        difference = numbers[-1] - numbers[0]
        if difference < 0:
            # This is a check for the smallest two numbers
            return numbers[0], numbers[1]
        elif difference > 0:
            # This is a check for the largest two numbers
            return numbers[-1], numbers[-2]
        else:
            # If the difference is 0, the closest numbers are the two middle numbers
            return numbers[len(numbers) // 2 - 1], numbers[len(numbers) // 2]