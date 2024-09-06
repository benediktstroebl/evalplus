from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    nums = sorted(numbers)
    leftend = 0
    rightend = len(nums) - 1
    while leftend < rightend:
        mid = (leftend + rightend) // 2
        if nums[mid] == nums[rightend]:
            # If the right end and mid are the same, we'll have to move it to the left
            rightend -= 1
        elif nums[mid] > nums[rightend]:
            # The mid is smaller than the right end, it is to the left of rightend
            rightend = mid
        else:
            # The mid is greater than the right end, it is to the right of rightend
            rightend = mid + 1
    return (nums[leftend], nums[rightend])

