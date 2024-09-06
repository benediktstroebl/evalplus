from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements more than once from a list of integers
        Returns a new list without duplicates, keeping the order of elements.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result