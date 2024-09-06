from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = nums_sorted[1] - nums_sorted[0]
    for i in range(1, len(nums_sorted)):
        current_diff = nums_sorted[i] - nums_sorted[i - 1]
        if abs(diff) > abs(current_diff):
            diff = current_diff
    return nums_sorted[0], nums_sorted[1]