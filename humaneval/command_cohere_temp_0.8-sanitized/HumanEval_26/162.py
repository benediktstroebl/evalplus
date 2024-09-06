from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements more than once in a list of integers and keeps the order intact. """
    return list(set(numbers))