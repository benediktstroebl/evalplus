from typing import List, Tuple
def rolling_max(numbers: List[int], target: Tuple[int, int]) -> List[int]:
    """ Returns the rolling maximum elements in the list of numbers as a list 
    until the target position given by the abscissa, ordinate tuple."""
    result = [num for num in numbers if num >= target[1]]
    return result
numbers = [1, 2, 3, 2, 3, 4, 2]