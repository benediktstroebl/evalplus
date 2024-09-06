from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements more than once from a list of integers. """
    return list(set(numbers))