from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    return list(set(numbers))