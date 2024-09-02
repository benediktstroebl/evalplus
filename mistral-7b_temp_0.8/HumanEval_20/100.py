from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    def find_closest(nums: List[float]) -> Tuple[float, float]:
        """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
        other and return them in order (smaller number, larger number).
        >>> find_closest([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
        """

        if len(nums) < 2:
            raise ValueError("There must be at least two elements in the list")

        diff = float("inf")
        min_diff = float("inf")

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if diff < abs(nums[i
