from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = nums_sorted[1] - nums_sorted[0]
    for i in range(1, len(nums_sorted)):
        if i == 1 or nums_sorted[i] - nums_sorted[i-1] != diff:
            first, second = nums_sorted[0], nums_sorted[i]
            return first, second
    else:
        return nums_sorted[0], nums_sorted[-1]