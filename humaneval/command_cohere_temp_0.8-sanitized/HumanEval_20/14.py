from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_set = set(numbers)
    if len(nums_set) < 2:
        raise ValueError("Input list of numbers must have at least two elements")

    candidates = []
    for x in nums_set:
        # Find closest number to x in nums_set
        closest = min(nums_set, key=lambda y: abs(x - y))
        candidates.append((x, closest))

    # Return the closest pair - simplest way is to just take the pair with minimum distance
    return min(candidates)[1:]