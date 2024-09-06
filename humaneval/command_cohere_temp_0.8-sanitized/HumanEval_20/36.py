def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = abs(nums_sorted[-1] - nums_sorted[0])
    return nums_sorted[0], nums_sorted[-1] if diff == min(diff, *[abs(nums_sorted[i] - nums_sorted[i-1]) for i in range(1, len(nums_sorted))]) else nums_sorted[1], nums_sorted[0]