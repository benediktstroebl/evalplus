from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        difference = numbers[-1] - numbers[0]
        if difference == 0:
            return numbers[0], numbers[0]
        elif difference > 0:
            for i in range(1, len(numbers)):
                if numbers[i] - numbers[i - 1] < difference:
                    difference = numbers[i] - numbers[i - 1]
                    smaller, larger = numbers[i - 1], numbers[i]
        else:
            for i in range(len(numbers) - 2, -1, -1):
                if numbers[i + 1] - numbers[i] < difference:
                    difference = numbers[i + 1] - numbers[i]
                    smaller, larger = numbers[i], numbers[i + 1]
        return smaller, larger