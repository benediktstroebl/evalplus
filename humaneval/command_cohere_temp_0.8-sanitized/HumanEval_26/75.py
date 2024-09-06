from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order as input. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not seen.add(num):
            result.append(num)
    return result