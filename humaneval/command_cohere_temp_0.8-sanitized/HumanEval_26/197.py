from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements more than once in a list of integers
        Returns a new list with order preserved from the input
    """
    return list(set(numbers))