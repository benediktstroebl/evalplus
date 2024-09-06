from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        difference = numbers[-1] - numbers[0]
        if difference == 0:
            return numbers[0], numbers[1]
        else:
            for i in range(1, len(numbers)):
                if numbers[i] - numbers[i - 1] == difference:
                    return numbers[i - 1], numbers[i]
            else:
                return numbers[0], numbers[-1]