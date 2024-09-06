from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    if delta == 0:
        return numbers[0], numbers[0]
    elif delta > 0:
        for i in range(1, len(numbers)):
            if numbers[i] - numbers[i - 1] == delta:
                return numbers[i - 1], numbers[i]
            elif numbers[i] - numbers[i - 1] < delta:
                delta = numbers[i] - numbers[i - 1]
                nearest_index_1 = i - 1
                nearest_index_2 = i
    elif delta < 0:
        for i in range(1, len(numbers)):
            if numbers[i - 1] - numbers[i] == delta:
                return numbers[i - 1], numbers[i]
            elif numbers[i - 1] - numbers[i] < delta:
                delta = numbers[i - 1] - numbers[i]
                nearest_index_1 = i - 1
                nearest_index_2 = i
    return numbers[nearest_index_1], numbers[nearest_index_2]