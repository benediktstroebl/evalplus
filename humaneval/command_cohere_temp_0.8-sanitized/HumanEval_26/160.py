from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements more than once, and keeps the order of remaining elements the same. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result