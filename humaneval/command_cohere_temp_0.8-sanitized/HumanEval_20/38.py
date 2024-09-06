from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    for i in range(1, len(numbers)):
        curr_delta = numbers[i] - numbers[i - 1]
        if curr_delta < delta:
            delta = curr_delta
    return numbers[0], numbers[-1]