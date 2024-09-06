from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_set = set(numbers)
    if len(nums_set) < 2:
        raise ValueError("Input list of numbers must have at least two elements")

    # Sorting numbers in ascending order.
    sorted_nums = sorted(nums_set)

    # Taking the first and the last number in the sorted list.
    # These two will always be the closest to each other.
    return sorted_nums[0], sorted_nums[-1]