from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    delta = numbers[-1] - numbers[0]
    if delta > 0.00001 and delta < 0.1:
        return numbers[0], numbers[-1]
    else:
        middle = (numbers[0] + numbers[-1]) / 2
        idx_left = 0
        idx_right = len(numbers) - 1
        while idx_right - idx_left > 1:
            idx_mid = (idx_left + idx_right) // 2
            if (numbers[idx_mid] - middle) ** 2 > (numbers[idx_left] - middle) ** 2:
                idx_left = idx_mid
            else:
                idx_right = idx_mid
        return numbers[idx_left], numbers[idx_right]