from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result