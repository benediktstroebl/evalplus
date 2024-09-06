from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a minimum of two elements")
    elif len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        middle = numbers[(len(numbers) - 1) // 2]
        if numbers[0] == numbers[-1]:
            return numbers[0], middle
        else:
            elements = (middle, middle)
            n = len(numbers)
            for i in range(1, n - 1):
                if numbers[i] != numbers[i - 1] and numbers[i] != numbers[i + 1]:
                    elements = (numbers[i - 1], numbers[i + 1])
                    break
            return elements