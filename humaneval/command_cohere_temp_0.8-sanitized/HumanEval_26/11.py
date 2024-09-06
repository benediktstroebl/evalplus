from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not (num in result and result.index(num) == len(result) - 1):
            result.append(num)
            seen.add(num)
    return result