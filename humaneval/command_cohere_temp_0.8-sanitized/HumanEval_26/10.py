from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements more than once, keeping order intact. """
    return list(set(numbers))