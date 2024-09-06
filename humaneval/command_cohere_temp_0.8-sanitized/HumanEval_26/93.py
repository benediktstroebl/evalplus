from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without any duplicates, keeping the order of elements left as is.
    """
    return list(set(numbers))