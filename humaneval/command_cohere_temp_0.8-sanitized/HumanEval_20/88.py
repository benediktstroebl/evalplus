from typing import List, Tuple
import unittest
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_copy = sorted(numbers)
    return nums_copy[0], nums_copy[-1]