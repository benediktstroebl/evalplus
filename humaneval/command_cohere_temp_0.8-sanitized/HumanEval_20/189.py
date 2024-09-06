from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        difference = numbers[-1] - numbers[0]
        if difference < 0:
            # This is a check for the edge case wherein the list contains only negative numbers, or only positive numbers.
            raise ValueError("Please provide a list of numbers with content between 0 and positive infinity")
        else:
            return numbers[0], numbers[-1]